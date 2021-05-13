N,P = map(int ,input().split())
A = list(map(int ,input().split()))
odd = 0#奇数
even = 0#偶数
for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
com = [[0] * 55 for i in range(55)]
com[0][0] = 1
for i in range(1,55):
    com[i][0] = 1
    for j in range(1,55):
        com[i][j] = com[i-1][j-1] + com[i-1][j]
eval = 0
for i in range(even + 1):
    eval += com[even][i]
oval = 0

if P == 0:
    for i in range(odd+1):
        if i % 2 == 0:
            oval += com[odd][i]
else:
    for i in range(odd + 1):
        if i % 2 == 1:
            oval += com[odd][i]
print(eval * oval)
