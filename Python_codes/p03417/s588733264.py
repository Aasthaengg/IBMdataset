n, m = map(int, input().split())
ans = 0
if n > m:
    n, m = m, n
if n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    ans = max(0, m - 2)
elif n == 2 or m == 2:
    ans = 0
else:
    ans = (n - 2) * (m - 2)
print(ans)
