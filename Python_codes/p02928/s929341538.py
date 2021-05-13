N, K = map(int, input().split())
A = list(map(int, input().split()))
M = 10**9+7
from collections import defaultdict

d = defaultdict(int)

lcl_cnt = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i] > A[j]:
            d[A[i]]+=1

            if i < j:
                lcl_cnt += 1

ans = lcl_cnt * K

for _, v in d.items():
    ans += (K-1)*v*K//2%M
    
print(ans%M)