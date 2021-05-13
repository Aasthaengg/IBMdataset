n, a, b = map(int, input().split())
if (b - a) % 2 == 0:
    ans = (b - a) // 2
else:
    ta = a + ((b - a - 1) // 2)
    tb = n - b + 1 + ((b - a - 1) // 2)
    ans = min(ta, tb)
print(ans)
