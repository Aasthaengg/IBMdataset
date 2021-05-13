N = int(input())
grid_a, grid_b = (list(map(int, input().split())) for _ in range(2))
table_a = []
tmp = 0
for i in grid_a:
    tmp += i
    table_a.append(tmp)
table_b = []
tmp = sum(grid_b)
for i in grid_b:
    table_b.append(tmp)
    tmp -= i
ans = 0
for i in range(N):
    ans = max(ans, table_a[i] + table_b[i])
print(ans)
