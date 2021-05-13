n = input()
l = len(n)

table = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if l == 1:
            if i + 1 <= int(n) and i == j:
                table[i][j] += 1
        elif l == 2:
            if 10 * (i + 1) + (j + 1) <= int(n):
                table[i][j] += 1
            if i == j:
                table[i][j] += 1
        else:
            if i + 1 < int(n[0]):
                for k in range(l-1):
                    table[i][j] += 10 ** k
            elif i + 1 == int(n[0]):
                if j + 1 <= int(n[-1]):
                    table[i][j] += int(n[1:l-1]) + 1
                else:
                    table[i][j] += int(n[1:l-1])
                for k in range(l-2):
                    table[i][j] += 10 ** k
            else:
                for k in range(l-2):
                    table[i][j] += 10 ** k
            if i == j:
                table[i][j] += 1

res = 0
for i in range(9):
    for j in range(9):
        res += table[i][j] * table[j][i]

print(res)