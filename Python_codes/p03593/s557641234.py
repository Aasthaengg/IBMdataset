
from collections import defaultdict

H,W = map(int, input().split())
S = [input() for _ in range(H)]

# Aが一文字だけの場合
if H == 1 and W == 1:
    print("Yes")
    exit()

d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[S[i][j]] += 1

# 普通の回分の場合
if H == 1 or W == 1:
    # 文字列が偶数個の場合は、それぞれの文字が偶数回出現していればOK
    if H % 2 == 0 or W % 2 == 0:
        f = True
        for i in d.values():
            if i % 2 != 0:
                f = False
        print("Yes" if f else "No")
    # 文字列が奇数個の場合、一つだけ奇数個の文字がある
    else:
        cnt_odd = 0
        for i in d.values():
            if i % 2 != 0:
                cnt_odd += 1
        print("Yes" if cnt_odd == 1 else "No")
# 行列の回分の場合
# 奇数×奇数のとき、行列の縦と横の真ん中の線の交点に来る文字は奇数個でOK。交点以外の真ん中のライン上の文字は２の倍数個いる。それ以外の位置は４の倍数個いる。
# 奇数×偶数でもおんなじ感じ
# 偶数×偶数は全部４の倍数個ずつ必要
else:
    #
    cnt_m1 = 0
    cnt_m2 = 0
    cnt_m3 = 0
    for i in d.values():
        if i % 4 == 1:
            cnt_m1 += 1
        elif i % 4 == 2:
            cnt_m2 += 1
        elif i % 4 == 3:
            cnt_m3 += 1
            
    f = True
    if H % 2 == 1 and W % 2 == 1:
        if cnt_m1 + cnt_m3 != 1:
            f = False
        if cnt_m2 + cnt_m3 > (H-1)//2 + (W-1)//2:
            f = False

    elif H % 2 == 1 or W % 2 == 1:
        if cnt_m1 != 0:
            f = False
        if H % 2 == 1:
            if cnt_m2 > (W//2):
                f = False
        else:
            if cnt_m2 > (H//2):
                f = False
        if cnt_m3 != 0:
            f = False
    else:
        if cnt_m1 != 0:
            f = False
        if cnt_m2 != 0:
            f = False
        if cnt_m3 != 0:
            f = False

    print("Yes" if f else "No")
