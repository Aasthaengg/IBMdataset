A = []
is_checked = []
res = False

for i in range(3):
    A.append(list(map(int, input().split())))

N = int(input())

b = {int(input()) for i in range(N)}

for i in range(3):
    is_checked.append([False]*3)
    for j in range(3):
        if A[i][j] in b:
            is_checked[i][j] = True

for i in range(3):
    if is_checked[i][0] and is_checked[i][1] and is_checked[i][2]:
        res = True
    if is_checked[0][i] and is_checked[1][i] and is_checked[2][i]:
        res = True

if is_checked[0][0] and is_checked[1][1] and is_checked[2][2]:
    res = True
if is_checked[0][2] and is_checked[1][1] and is_checked[2][0]:
    res = True

print(['No', 'Yes'][res])