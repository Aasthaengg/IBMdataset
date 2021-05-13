##### 解けた #####

A,B,C,D=list(map(int,input().split(" ")))
wL=A+B # 左の皿
wR=C+D # 右の皿

if wL<wR: # 右に傾く場合
    print("Right")
elif wL>wR: # 左に傾く場合
    print("Left")
elif wL==wR:
    print("Balanced")