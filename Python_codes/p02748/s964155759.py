A, B, M = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
ans = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    tmp = a[x - 1] + b[y - 1] - c
    ans = min(ans, tmp)
print(ans)
