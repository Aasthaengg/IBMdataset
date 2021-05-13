A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 10**6

for _ in range(M):
    x, y, c = map(int, input().split())
    res = min(a[x-1]+b[y-1]-c, res)

a.sort()
b.sort()
print(min(res, a[0]+b[0]))