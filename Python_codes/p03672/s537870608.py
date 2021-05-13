S = input().strip()
N = len(S)
for i in range(N//2-1,0,-1):
    if S[:i]==S[i:2*i]:
        ans = i
        break
print(ans*2)