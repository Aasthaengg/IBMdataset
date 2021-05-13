n, m = map(int, open(0).read().split())
if 2*n <= m:
    ans = n + (m - 2*n)//4
else:
    ans = m // 2
print(ans)