# -*- coding: utf-8 -*-
import sys
import itertools#これは色々使える組み込み関数みたいなやつ
import math#数学的計算はこれでいける。普通に0.5乗しても計算可能
#w=input()
A, B, C, K=input().split()
A=int(A)
B=int(B)
C=int(C)
K=int(K)
i=0
ID_list=[]
ID_sublist=[]
gate_possible_list=[]
A_dummy=0
B_dummy=0
C_dummy=0
#センテンスを暗記するのではなく、まずinput()を書いて、膨らます感じで記述する。すると#思考の流れ通りに書ける。素晴らしい！
#for i in range(K):
# ID_list.append(i+1)
#print(ID_list)
#for i in range(N)
#gate_list =  [list(map(int, input().split(" ")))for i in range(M)]
#センテンスを暗記するのではなく、まずinput()を書いて、膨らます感じで記述する。すると#思考の流れ通りに書ける。素晴らしい！

#x=[]
#y=[]
#t, x, y = [0]*(N+1), [0]*(N+1), [0]*(N+1)#N+1個の空のリストを作成(原点を入れて##るから一つ増える)
#delta_t=0
#delta_x=0
#delta_y=0
#l=0
#t[0],x[0],y[0]=[0, 0, 0]
#とりあえず入力までは完成した．
#for i in range(N):
# t[i+1], x[i+1], y[i+1] = map(int, input().split())
#child_i =  list(map(int, input().split()))
#w_len=len(w)
#w_list=list(w)
#print(len(w_list))
#print(w_list)
#child_il=sorted(child_i)
#print(child_il)#リストの右端のほうが大きい
i=0
if A==B==C:
    print(0)
    sys.exit()
#for i in range(K):
#    A_dummy=B+C
#    B_dummy=A+C
#    C_dummy=A+B
#    A=A_dummy
#    B=B_dummy
#    C=C_dummy

if abs(A-B)>10**18:
    print("Unfair")
    sys.exit()

if K%2==0:
    print(A-B)
    sys.exit()

if K%2==1:
    print(-(A-B))
    sys.exit()
