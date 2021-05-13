x, k, d = map(int, input().split())

x = abs(x)
if x ==0:
    ans = d * (k % 2)
elif x - d * k  >= 0:
    ans = x - d * k
else:
    if abs(x - x // d * d) <= abs(x - (x // d + 1) * d):
        div = x // d
    else:
        div = x // d + 1
    if (k - div) % 2 == 0:
        ans = abs(x - d * div)
    else:
        ans = min(abs(x - d * div + d),abs(x - d * div - d))
print(ans)