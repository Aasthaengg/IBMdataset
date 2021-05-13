n = int(input())
hort = [[0] * 9 for i in range(9)]
#hort[i][j] := i~j
for i in range(1, n + 1):
    temp = str(i)
    if temp[0] == '0' or temp[-1] == '0':continue 
    hort[int(temp[0]) - 1][int(temp[-1]) - 1] += 1

res = 0
for i in range(9):
    for j in range(9):
        if i != j:
            temp = hort[i][j] * hort[j][i] * 2
        else:
            temp = hort[i][j] * (hort[i][j] - 1) + hort[i][j]
            #print(temp, i, j)
        hort[i][j] = 0
        res += temp

print(res)