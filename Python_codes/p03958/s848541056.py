K, T = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = (A[-1] - 1) - (K-A[-1])
print(max(ans, 0))