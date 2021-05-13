x, k, d = map(int, input().split())

x = abs(x)
div = min(x//d, k)
if (k - div) % 2 == 0:
    ans = abs(x - d * div)
else:
    ans = abs(x - d * div - d)
print(ans)