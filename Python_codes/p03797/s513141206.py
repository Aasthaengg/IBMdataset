n, m = map(int, input().split())

if n*2 < m:
    c = m - (n*2)
    ans = int(c/4) + n
else:
    ans = int(m/2)

print(ans)