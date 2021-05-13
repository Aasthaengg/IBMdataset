#B

import numpy as np
D = int(input())
C = list(map(int,input().split()))
S = np.empty((D,26))
for i in range(D):
    l = list(map(int,input().split()))
    for j in range(26):
        S[i][j] = l[j]
        
#開催日時の記録
R = np.zeros(26)

sc = 0

#与えられたtでスコアを計算
for i in range(1,D+1):
    
    #ランダムに開催するコンテストを選ぶ
    con = int(input()) - 1
    
    #スコア計算
    #コンテスト開催による上昇
    sc += S[i-1][con]
    R[con] = i
    
    #コンテスト非開催による減少
    for j in range(26):
        sc -= C[j]*(i-R[j])
        
    print(int(sc))