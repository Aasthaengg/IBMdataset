a, b, k = map(int, input().split())
if k <= a:
    ans = (a-k, b)
else:
    ans = (0, max(0, a+b-k))
print(*ans, sep=' ')