


X,Y,A,B,C = map(int, input().split())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

red_green = [(p, "r") for p in P] + [(q, "g") for q in Q]
red_green.sort()
nc = R
nc.sort()

cnt_r , cnt_g , cnt_n = 0,0,0

ans = 0
while cnt_r + cnt_g + cnt_n < X + Y:

    # 指定の個数食べきっている色は除外
    if cnt_r == X:
        while red_green[-1][1] == "r":
            red_green.pop()
    if cnt_g == Y:
        while red_green[-1][1] == "g":
            red_green.pop()

    # 無色と色付きの得点の高いほうを食べる
    if len(nc) > 0 and nc[-1] > red_green[-1][0]:
        point = nc.pop()
        ans += point
        cnt_n += 1
    else:
        point, color = red_green.pop()
        ans += point
        if color == "r":
            cnt_r += 1
        else:
            cnt_g += 1


print(ans)