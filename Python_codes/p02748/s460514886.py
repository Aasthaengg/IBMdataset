_, _, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mi = 10**6
for _ in range(m):
    x, y, c = map(int, input().split())
    mi = min(mi, a[x-1] + b[y-1] - c)
print(min(mi, min(a)+min(b)))