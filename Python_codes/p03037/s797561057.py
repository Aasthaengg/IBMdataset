n, m = map(int, input().split())
l, r = map(int, input().split())

for _ in range(m - 1):
    a, b = map(int, input().split())
    l = max(l, a)
    r = min(r, b)

print(max(0, r - l + 1))
