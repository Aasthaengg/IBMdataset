# -*- coding: utf-8 -*-
N="0"+raw_input()
l=len(N)

F=[ 0 for _ in range(l) ] #繰り上がりなし
T=[ 0 for _ in range(l) ] #繰り上がりあり
#初期化
x=int(N[l-1])
F[l-1]=x
T[l-1]=10-x

for i in range(l-1,0,-1):
    next_x=int(N[i-1])
    #繰上なしへの遷移。前の桁が繰上なしの場合は単に該当桁の数字を足す、
    #前の桁が繰上ありの場合は、今の桁の数字が1増える
    F[i-1]=min(F[i]+next_x, T[i]+next_x+1) 
    #繰上ありへの遷移。前の桁が繰上なしの場合は(10-該当桁の数字)を足す、
    #前の桁が繰上ありの場合は今の桁の数字が1増えているので(10-該当桁の数字+1)
    T[i-1]=min(F[i]+10-next_x, T[i]+10-(next_x+1))

print F[0]
