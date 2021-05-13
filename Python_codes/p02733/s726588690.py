H, W, K = map(int, input().split())

G = [list(input()) for _ in range(H)]

ans = H * W

def calc(lst):
    group = sum(lst) + 1
    tmp = [[0] * W for _ in range(group)] #何グループに分かれるか
    k = 0
    for j in range(W):
        for i in range(H):
            if G[i][j] == '1':
                tmp[k][j] += 1
            if lst[i] == 1 or i == H - 1:
                k = (k + 1) % group
    
    cut = group - 1
    for j in range(W):
        flag = False
        for i in range(group):
            if tmp[i][j] > K:
                return 10 ** 9
            if j < W - 1:
                if tmp[i][j] + tmp[i][j + 1] > K: #次の戸合わせてKより大きくなるなら切る
                    flag = True
        if flag:
            cut += 1
        else:
            for i in range(group):
                if j < W - 1:
                    tmp[i][j + 1] += tmp[i][j]
    return cut


for i in range(2 ** (H - 1)): #ビットでカットするラインを探索
    lst = [0] * H
    for j in range(H - 1):
        if (i >> j) & 1: #切れるとき
            lst[j] = 1
    # print (lst)
    ans = min(ans, calc(lst))

print (ans)
    
