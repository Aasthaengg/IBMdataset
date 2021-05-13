Height, Width = map(int, input().split())

minse=[]

for i in range(Height):
    mine = list(input())
    minse.append(mine)

ans_list = [[0 for j in range(Width)] for i in range(Height)]


for h in range(Height):
    for w in range(Width):
        me = minse[h][w]
        if (me == '#'):

            for i in range(3):
                for j in range(3):
                    if (i != 1 or j != 1):
                        index_h = h - 1 + j
                        index_w = w - 1 + i
                        if (index_h < Height and index_h >=0 and index_w>=0 and index_w < Width):
                            ans_list[index_h][index_w] += 1
                            

for i in range(Height):
    for j in range(Width):
        value = minse[i][j]
        if (value == '#'):
            ans_list[i][j]='#'

for i in range(Height):
    tmp = ans_list[i]
    print(''.join(map(str,tmp)))