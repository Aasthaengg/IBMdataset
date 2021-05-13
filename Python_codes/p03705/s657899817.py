n, a, b = map(int, input().split())
M = b*(n-1)+a
m = b+a*(n-1)
print(max(M-m+1, 0))
