n, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    if l[i][0] >= x and l[i][1] >= y:
        ans += 1
print(ans)