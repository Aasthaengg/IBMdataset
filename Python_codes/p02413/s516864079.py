(r, c) = [int(i) for i in input().split()]

table = []
for rc in range(r):
    table.append([int(i) for i in input().split()])

table.append([0 for _ in range(c + 1)])

for rc in range(r):
    row_total = 0
    for cc in range(c):
        table[r][cc] += table[rc][cc]
        row_total += table[rc][cc]

    table[rc].append(row_total)
    table[r][c] += row_total

for row in table:
    print(' '.join([str(column) for column in row]))