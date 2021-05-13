r, c = map(int, raw_input().split(" "))
table1 = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    table1[i] = map(int, raw_input().split(" "))

table2 = [[0 for j in range(c+1)] for i in range(r+1)]
for i in range(r):
    for j in range(c):
        table2[i][j] = table1[i][j]

for i in range(r):
    for j in range(c):
        table2[i][c] += table2[i][j]
        table2[r][j] += table2[i][j]
    table2[r][c] += table2[i][c]

ans = ""
for i in range(r+1):
    for j in range(c+1):
        ans += str(table2[i][j])
        if j!=c:
            ans += " "
    if i!=r:
        ans += "\n"

print ans