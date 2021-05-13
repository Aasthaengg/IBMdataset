from collections import defaultdict
N,p = map(int,input().split())

S = input()[::-1]

d = {}

ans = 0
if p == 2:
    for i in range(N):
        if S[i] in ['0','2','4','6','8']:
            ans += N-i
elif p==5:
    for i in range(N):
        if S[i] in ['0','5']:
            ans += N-i
else:
    d = defaultdict(lambda:0)
    n = 0
    for i in range(N):
        n += pow(10,i,p)*int(S[i])
        n %= p
        d[n] += 1
    ans += d[0]
    for k in d:
        ans += d[k]*(d[k]-1)//2
print(ans)