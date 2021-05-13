
from collections import defaultdict


N,P = map(int, input().split())
S = input()
ans = 0
if P in [2,5]:
    
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i + 1

else:
    d = defaultdict(int)
    d[0] = 1
    curr = 0
    for i in range(N):
        curr = curr + int(S[N-1-i]) * pow(10, i, P)
        curr %= P
        ans += d[curr]
        d[curr] += 1

print(ans)