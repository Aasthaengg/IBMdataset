n, m, d = map(int,input().split())
ans = 2 * (m - 1) * (n - d) / n ** 2
if d == 0:
    ans /= 2
print(ans)