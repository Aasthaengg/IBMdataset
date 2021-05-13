import itertools
import bisect
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

a = [0] + list(itertools.accumulate(A))
b = [0] + list(itertools.accumulate(B))

result = 0
for i in range(N + 1):
    if a[i] > K:
        break
    j = bisect.bisect_right(b, K - a[i])
    result = max(result, i + j - 1)
print(result)