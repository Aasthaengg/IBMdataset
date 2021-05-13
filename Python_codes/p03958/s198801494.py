k, t = map(int, input().split())
L = list(map(int, input().split()))
M = max(L)
print(max(0, M - (k - M) - 1))
