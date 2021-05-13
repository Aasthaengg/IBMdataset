from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = ceil((N-1)/(K-1))
print(ans)
