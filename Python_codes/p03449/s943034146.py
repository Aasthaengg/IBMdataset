# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:46:33 2020

@author: naoki
"""

N = int(input()) # 横列の数N
array1 = list(map(int,input().split())) # 1行目のアメの数を入力
array2 = list(map(int,input().split())) # 2行目のアメの数を入力
#どの段階で下の行に移るかが問題でアメの取り方はN通りある
count = [0 for i in range(N)] # 取った雨の数の合計を格納する配列。

for k in range(N): # k列目で下の行に移った場合
    i = 0
    j = k
    while i <= k:
        count[k] = count[k] + array1[i] 
        i+=1            
        while j <= N-1:
            count[k] = count[k] + array2[j]
            j+=1
count.sort(reverse = True)

print(count[0])