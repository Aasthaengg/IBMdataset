h, w = map(int, input().split())
S = [["#"] * (w + 2)]
for i in range(h):
    S.append(["#"] + list(input()) + ["#"])
S.append(["#"] * (w + 2))
Lamp_row = [[0 for i in range(w+2)] for j in range(h+2)]
Lamp_col = [[0 for i in range(w+2)] for j in range(h+2)]
#print(S)

for row in range(h + 2):
    counter = 0
    for col1 in range(w + 1):
        col2 = col1 + 1
        if S[row][col1] == "#" and S[row][col2] == ".":
            start = col2
            counter += 1
        if S[row][col1] == "." and S[row][col2] == ".":
            counter += 1
        if S[row][col1] == "." and S[row][col2] == "#":
            end = col2
            for i in range(start, end):
                Lamp_row[row][i] = counter
            counter = 0
#print(*Lamp_row, sep="\n")
#print()

for col in range(w + 2):
    counter = 0
    for row1 in range(h + 1):
        row2 = row1 + 1
        if S[row1][col] == "#" and S[row2][col] == ".":
            start = row2
            counter += 1
        if S[row1][col] == "." and S[row2][col] == ".":
            counter += 1
        if S[row1][col] == "." and S[row2][col] == "#":
            end = row2
            for i in range(start, end):
                Lamp_col[i][col] = counter
            counter = 0
#print(*Lamp_col, sep="\n")

max_sum = 0
for row in range(h+2):
    for col in range(w+2):
        max_sum = max(max_sum, Lamp_row[row][col] + Lamp_col[row][col] - 1)
print(max_sum)