# import numpy as np
# import scipy as sp
# import sys
# input = sys.stdin.readline
# print(a,b,c,sep="") # 半角スペースなしで出力(abc)
# n=int(input())  #数値入力 「N」だけの入力のとき
# a,b=list(map(int, input().split()))  #複数数値入力　「A B」みたいなスペース空いた入力のとき
# a=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき
# a=[int(input()) for _ in range (n)]  #リスト入力  改行でa1 ... anのとき
# s=[list(map(str,list(input()))) for i in range(h)]  # 文字列の二次元配列入力
# s = [list(map(int, input().split())) for i in range(n)] # 数値の二次元配列入力
# a = b[:], a = [x[:] for x in b] # deepcopy
# chr(ord('a') + 1) # chrのインクリメント
# s.sort(key=lambda x: x[1], reverse=False) # 2番目の要素で昇順にソート（Trueなら降順）
#　

import itertools
import bisect
n, m = list(map(int, input().split()))
al = list(map(int, input().split()))
al.sort()
ub = al[-1]*3
lb = -1
while lb + 1 < ub:
    target = (ub+lb)//2
    tmp = 0
    for a in al:
        sa = target - a
        # リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す
        i = bisect.bisect_left(al, sa)
        tmp += (n-i)
    if (tmp >= m):
        lb = target
    else:
        ub = target


rui_al = [0] + list(itertools.accumulate(al))
ans = 0
tmp = 0
target = lb
for a in al:
    sa = target - a
    # リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す
    i = bisect.bisect_left(al, sa)
    tmp += (n-i)
    ans += (rui_al[-1] - rui_al[i])
    ans += a*(n-i)

if tmp > m:
    ans -= (tmp-m)*target
print(ans)
