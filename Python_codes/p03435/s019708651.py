c = [list(map(int, input().split())) for _ in range(3)]

a1 = 0
b1 = c[0][0] - a1
b2 = c[0][1] - a1
b3 = c[0][2] - a1
a2 = c[1][0] - b1
a3 = c[2][0] - b1

ans = [
    [a1+b1, a1+b2, a1+b3],
    [a2+b1, a2+b2, a2+b3],
    [a3+b1, a3+b2, a3+b3]
]

for i in range(3):
    for j in range(3):
        if c[i][j] == ans[i][j]:
            pass
        else:
            print('No')
            exit()
print('Yes')