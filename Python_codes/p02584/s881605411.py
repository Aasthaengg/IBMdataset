x, k, d = map(int, input().split())
x = abs(x)
ans = 0
if x >= k * d:
    ans = x - d * k
else:
    i = x // d
    j = k - i
    if (j % 2 == 0):
        ans = x - d * i
    else:
        ans = x - d * (i + 1)
print(abs(ans))