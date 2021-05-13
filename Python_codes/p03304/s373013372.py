n, m, d = map(int, input().split())
ans = (2*n - min(2*d, n)) * (m - 1) / (n**2)
if d == 0: ans /= 2
print(format(ans, '.10f'))