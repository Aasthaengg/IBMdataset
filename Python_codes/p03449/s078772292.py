n = int(input())
field = [list(map(int, input().split())) for _ in range(2)]
ans = []
field_0 = 0
field_1 = 0

for i in range(n):
    field_0 += field[0][i]

    for j in range(i, n):
        field_1 += field[1][j]
    
    ans.append(field_0 + field_1)
    field_1 = 0
print(max(ans))
