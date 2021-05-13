n, m = [int(x) for x in input().split()]
if n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    ans = max(n, m) - 2
else:
    ans = n * m - 2 * n - 2 * m + 4
print(ans)