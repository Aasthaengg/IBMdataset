K, T = map(int, input().split())
a = list(map(int, input().split()))

M = max(a)
ans = max(M - 1 - (K - M), 0)
print(ans)