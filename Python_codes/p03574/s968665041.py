# -*- coding: utf-8 -*-

H, W = map(int, input().split())

S = []
ans_S = []

for i in range(H):
    tmp_s = list(str(input()))
    S.append(tmp_s)
    ans_S.append(tmp_s)

for y in range(H):
    for x in range(W):
        tmp_ans_S = 0
        if S[y][x] == '#':
            tmp_ans_S = '#'
        else:
            # 1 左
            if x > 0:
                if S[y][x - 1] == '#':
                    tmp_ans_S += 1 
            # 2 左上
            if x > 0 and y > 0:
                if S[y - 1][x - 1] == '#':
                    tmp_ans_S += 1
            # 3 上
            if y > 0:
                if S[y - 1][x] == '#':
                    tmp_ans_S += 1
            # 4 右上
            if x < (W - 1) and y > 0:
                if S[y - 1][x + 1] == '#':
                    tmp_ans_S += 1
            # 5 右
            if x < (W - 1):
                if S[y][x + 1] == '#':
                    tmp_ans_S += 1
            # 6 右下
            if x < (W - 1) and y < (H - 1):
                if S[y + 1][x + 1] == '#':
                    tmp_ans_S += 1
            # 7 下
            if y < (H - 1):
                if S[y + 1][x] == '#':
                    tmp_ans_S += 1
            # 8 左下
            if x > 0 and y < (H - 1):
                if S[y + 1][x - 1] == '#':
                    tmp_ans_S += 1
        # ヒトマスごとに集計した分の挿入
        ans_S[y][x] = tmp_ans_S

for ans in ans_S:
    print(*ans, sep='')