an, bn, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = min(a) + min(b)
for i in range(m):
    x, y, c = map(int, input().split())
    r = min(r, a[x-1] + b[y-1] - c)

print(r)

