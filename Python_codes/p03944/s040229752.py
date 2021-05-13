def resolve():
    W, H, N = list(map(int, input().split()))
    # (0,0)(W,H)を含む交点のx,y座標リスト
    white_W_list = list(range(W+1))
    white_H_list = list(range(H+1))
    for i in range(N):
        x, y, a = list(map(int, input().split()))
        if a == 1:
            white_W_list = [j for j in white_W_list if j >= x]
        elif a == 2:
            white_W_list = [j for j in white_W_list if j <= x]
        elif a == 3:
            white_H_list = [j for j in white_H_list if j >= y]
        elif a == 4:
            white_H_list = [j for j in white_H_list if j <= y]
    width = len(white_W_list) - 1
    length = len(white_H_list) - 1
    if width >= 1 and length >= 1:
        area = width * length
        print(area)
    else:
        print(0)

resolve()