n, m = [int(i) for i in input().split()]
ans = 0
diff = m - n
if diff >= 2:
    x = n * 2
    y = m - x
    ans += n
    ans += y // 4
else:
    ans = m // 2
print(ans)
