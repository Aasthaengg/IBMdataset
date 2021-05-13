# -*- coding: utf-8 -*-
import sys
from itertools import combinations
# 標準入力を受け取る
n = int(input())
### 奇数処理
if n % 2 == 1:
    ### NGな組み合わせは奇数の時{i,N-i}
    ### (1，N-1),(２，N-2),(3，N-3)・・・(i，N-i)・・・,(N-1,1),N
    ### NGな組み合わせは全部でN個、最後はN単独なので除外(-1)。半分は入れ替わっただけで同じ組み合わせなので半分。
    ### NGな組み合わせの数を計算する
    # ng = (n-1)/2
    # m = n(n-1)/2 - ng
    ## 上の式を整理して下記
    m = (n-1)*(n-1)/2
    print(int(m))
    ### グラフを表示する
    for i, j in combinations(range(1,n+1),2):
        if (i + j) != n:
            print(i, j)
### 偶数処理
else:
    ### NGな組み合わせは偶数の時{i,N-i+1}
    ### (1,N),(2,N-1),(3,N-2)・・・(i，N-i+1)・・・,(N-1,2),(N,1)
    ### NGな組み合わせは全部でN個、半分は入れ替わっただけで同じ組み合わせなので半分。
    ### NGな組み合わせの数を計算する
    #ng = n/2
    #m = n(n-1)/2 - ng
    ## 上の式を整理して下記
    m = (n-2)*n/2
    print(int(m))
    ### グラフを表示する
    for i, j in combinations(range(1,n+1),2):
        if (i + j) != n+1:
            print(i, j)
