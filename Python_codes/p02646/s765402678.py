info_A = input().split()
info_B = input().split()
T = int(input())
win = ''

A = int(info_A[0]) #A（鬼）の開始位置
V = int(info_A[1]) #A（鬼）の速度
B = int(info_B[0]) #B（逃げる側）の開始位置
W = int(info_B[1]) #B（逃げる側）の速度

# 逃げる側の速度が同じか速ければ追いつけない
if W >= V:
    win = 'B'

else:
# T秒後までに同じ座標にいればAが勝つ
    k = (B-A)/(V-W)
    if A>B:
        k = -k
    
    if k <= T and 0 < k:
        win = 'A'
    else:
        win = 'B'


if win == 'A':
    print('YES')
else:
    print('NO')