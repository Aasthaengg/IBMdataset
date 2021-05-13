lc = [[int(w) for w in input().split()] for i in range(3)]
cond = True

lb = lc[0]
a2 = lc[1][0]-lb[0]
a3 = lc[2][0]-lb[0]
la = [0, a2, a3]
for i in range(3):
    for j in range(3):
        if lc[i][j] != la[i]+lb[j]:
            cond = False
            break

print("Yes" if cond else "No")
