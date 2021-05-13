# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline().strip())
A=map(int, sys.stdin.readline().split())
A_max=max(A)
A_max_idx=A.index(A_max)    #0-indexed
A_min=min(A)
A_min_idx=A.index(A_min)    #0-indexed

if 0<=A_min:    #Aの最小値が0以上である場合、累積和を構成すれば良い
    print N-1
    for i in range(1,N):
        print i,i+1
else:    #Aの最小値が0より小さい場合
    if 0<=A_max:
        if abs(A_min)<=abs(A_max):  #絶対を取った時にA_maxがA_min以上
            print 2*N-1
            for i in range(1,N+1):  #A_maxを配列Aの全ての値にそれぞれ足していく
                print A_max_idx+1,i
            for i in range(1,N):    #その後に累積和を取れば良い
                print i,i+1
        elif abs(A_min)>abs(A_max):  #絶対を取った時にA_minがA_max以上
            print 2*N-1
            for i in range(1,N+1):  #A_minを配列Aの全ての値にそれぞれ足していって、aを全て負の数にする
                print A_min_idx+1,i
            for i in range(N,1,-1): #後ろから累積和
                print i,i-1
    elif A_max<0:   #aの値が全部負なので、後ろから累積和を取ればよい
        print N-1
        for i in range(N,1,-1): #後ろから累積和
            print i,i-1