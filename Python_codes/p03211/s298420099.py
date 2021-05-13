# B - 754
S = input()

def f(i):
    return abs(100*int(S[i])+10*int(S[i+1])+int(S[i+2])-753)

ans = 10000
for i in range(len(S)-2):
    ans = min(ans, f(i))
print(ans)