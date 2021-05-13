# import numpy as np
# import scipy as sp
# print(a,b,c,sep="") # 半角スペースなしで出力(abc)
# n=int(input())  #数値入力 「N」だけの入力のとき
# a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
# c=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき
# s=[list(map(int,list(input()))) for i in range(h)]  # 二次元配列入力　二次元マップみたいな入力のとき
# import sys ; sys.exit() # プログラム終了
# from copy import deepcopy ; b=deepcopy(a)
# chr(ord('a') + 1)
# s.sort(key=lambda x: x[1], reverse=False) # 2番目の要素で昇順にソート（Trueなら降順）
#
a = max(map(int, input().split()))
if a <= 8:
    ans = 'Yay!'
else:
    ans = ':('

print(ans)
