n, m = map(int,input().split())
ans = n * m
if n == 1 and m == 1:
    pass
elif n == 1 or m == 1:
    ans -= 2
else:
    ans -= 2 * (n + m) - 4
print(ans)