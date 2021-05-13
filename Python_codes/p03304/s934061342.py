#!/usr/bin/env python3
n,m,d = map(int,input().split())	
# abs(a[i]-a[i+1])のsum の平均を求める
# 1..n から構成される長さmの数列 pow(n,m)通りを並び替えた数列に対して平均を求める
# 総和を求めてpow(m,m)でわる
# 同じ数字を何回使っても良いから、それぞれの場所に対して何パターンあるかを計算して、
# それにpow(n,m-2)を欠けたものを足す感じでできる 平均は i,i+1のパターン / n^2
# if d == 1: *n 
# else: (n-d)*2
# 足す箇所はm-1あるので
k = 0
if d == 0: k = n
else: k = (n-d)*2
ans = (m-1)*k/(n**2)
print(ans)