n, m = map(int, input().split())
r = (n - 2) * (m - 2)
if (r < 0):
    r *= -1
print(r)