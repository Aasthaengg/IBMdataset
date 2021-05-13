from collections import defaultdict
import bisect
N,K = map(int,input().split())
A = list(map(int,input().split()))
S = [0]*N
for i in range(N):
    S[i] = S[i-1]+A[i]
    S[i] %= K
d = defaultdict(list)
for i in range(N):
    d[(S[i]-i)%K].append(i)

ans = 0
for k in d:
    l = d[k]
    for i in range(len(l)):
        n = l[i]
        j = bisect.bisect_left(l,n+K)
        ans += j-i-1
    if k==1:
        j = bisect.bisect_left(l,K-1)
        ans += j
            
print(ans)