l = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for bb in b:
    for i in range(3):
        for j in range(3):
            if l[i][j] == bb:
                ans[i][j] = 1

if ans[0][0] == ans[1][1] == ans[2][2] == 1:
    print('Yes')
elif ans[0][2] == ans[1][1] == ans[2][0] == 1:
    print('Yes')
elif ans[0][0] == ans[1][0] == ans[2][0] == 1:
    print('Yes')
elif ans[0][1] == ans[1][1] == ans[2][1] == 1:
    print('Yes')
elif ans[0][2] == ans[1][2] == ans[2][2] == 1:
    print('Yes')

elif ans[0][0] == ans[0][1] == ans[0][2] == 1:
    print('Yes')
elif ans[1][0] == ans[1][1] == ans[1][2] == 1:
    print('Yes')
elif ans[2][0] == ans[2][1] == ans[2][2] == 1:
    print('Yes')

else:
    print('No')
