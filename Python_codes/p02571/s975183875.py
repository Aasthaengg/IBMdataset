def count_diff(a,b):
    cnt = 0
    for c1,c2 in zip(a, b):
        if c1 != c2:
            cnt += 1
    return cnt

S = str(input())
T = str(input())
mn = 100000

for i in range(len(S)-len(T)+1):
    s = S[i:i+len(T)]
    x = count_diff(s,T)
    mn = min(mn,x)

print(mn)