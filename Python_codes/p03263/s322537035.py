H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
odd_num = 0
odd_point = []
for i in range(H):
    for j in range(W):
        if a[i][j] % 2:
            odd_num += 1
            odd_point += [[i, j]]
            a[i][j] = 1
        else:
            a[i][j] = 0

moves = []
i, j = 0, 0
direction = 1
while len(moves) < H*W-1:
    pre_i, pre_j = i, j
    if j+1 == W and direction == 1:
        i += 1
        direction *= -1
    elif j-1 == -1 and direction == -1:
        i += 1
        direction *= -1
    else:
        j += direction
    moves += [(pre_i, pre_j, i, j)]

flag = False
ans = []
for pre_i, pre_j, i, j in moves:
    if a[pre_i][pre_j] == 1:
        if flag == False:
            flag = True
        else:
            flag = False
    if flag:
        ans += [(pre_i+1, pre_j+1, i+1, j+1)]
print(len(ans))
for pre_i, pre_j, i, j in ans:
    print(pre_i, pre_j, i, j)