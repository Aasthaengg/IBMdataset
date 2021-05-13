A, B, M = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())
ans = 10**20

for _ in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, a[x-1]+b[y-1]-c)

a.sort()
b.sort()

ans = min(ans, a[0]+b[0])
print(ans)
