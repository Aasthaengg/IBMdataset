h, w, k = map(int, input().split())
mass = []
black_count = 0
ans = 0
for _ in range(h):
    row = list(input())
    mass.append(row)
    black_count += row.count("#")

goal = black_count - k    

for i in range(2**h):
    row_tmp = str(bin(i)).split("0b")[1]
    row_tmp = '0'*(h - len(row_tmp))+row_tmp
    for j in range(2**w):
        col_tmp = str(bin(j)).split("0b")[1]
        col_tmp = '0'*(w - len(col_tmp))+col_tmp
        
        row_count = 0
        col_count = 0
        for k in range(h):
            row_count += (mass[k] * int(row_tmp[k])).count("#")
        for k in range(h):
            for l in range(w):
                col_count += (mass[k][l] * (int(col_tmp[l]) * (1-int(row_tmp[k])))).count("#")
        if goal == row_count+ col_count:
            ans += 1
print(ans)