n, m = map(int, input().split())
if n > 1 and m > 1:
    ans = n * m - 2 * (n + m) + 4
elif n > 1:
    ans = n - 2
elif m > 1:
    ans = m - 2
else:
    ans = 1
print(ans)