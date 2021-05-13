N,M = map(int,input().split())
X = (N - M) * 100
Y = M * 1900
Z = X + Y
ans = Z * (2 ** M)
print(ans)
