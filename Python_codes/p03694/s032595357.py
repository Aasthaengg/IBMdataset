# -*- coding: utf-8 -*-
import sys
import itertools#これは色々使える組み込み関数みたいなやつ
#import math#数学的計算はこれでいける。普通に0.5乗しても計算可能
#w=input()
from operator import itemgetter
from sys import stdin
#input = sys.stdin.readline#こっちの方が入力が早いが使える時に使っていこう

N=3
M=3
i=0
j=0
k=0



N=int(input())
dis_list=[]
housepos_list=list(map(int, input().split(" ")))#数字の時
#ソートして小さい順から差を求めていけばいいか
housepos_list=sorted(housepos_list)
for i in range(N-1):
    dis_list.append(housepos_list[i]-housepos_list[i+1])
print(abs(sum(dis_list)))
#A=int(input())
#B=int(input())
#print(N)
"1行1つの整数を入力を取得し、整数と取得する"


#number_list=list(map(int, input().split(" ")))#数字の時
#print(number_list)
"12 21 332 とか入力する時に使う"
"1行に複数の整数の入力を取得し、整数として扱う"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#メモ
for i in number_list:#こっちの方がrage使うより早いらしい
    print(number_list[i-1])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
x=[]
y=[]
for i in range(N):
    x1, y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)
print(x)
print(y)
"複数行に2数値を入力する形式 x座標とy座標を入力するイメージ"
'''

'''
mixlist=[]
for i in range(N):
    a,b=input().split()
    mixlist.append((int(a),b))
print(mixlist)
"複数行にintとstrを複合して入力するやつ，今回はリスト一つで処理している"
'''

'''
#array=[input().split()for i in range(N)]
#print(type(array[0][0]))
#print(array)
"正方行列にstr型の値を入力"
'''

#brray=[list(map(int, input().split(" ")))for i in range(N)]
#print(type(brray[0][0]))
#print(brray)
'''
入力
1 2
4 5
7 8
出力結果
[[1, 2], [4, 5], [7, 8]]
'''
"列数に関して自由度の高いint型の値を入力するタイプの行列"
#以下に別解を記載
#N, M = [int(i) for i in input().split()]
'''
table = [[int(i) for i in input().split()] for m in range(m)]

print(type(N))
print(N)
print(type(M))
print(M)

print(type(table))
print(table)
'''




#s=input()
#a=[int(i) for i in s]
#print(a[0])
#print([a])
#単数値．桁ごとに分割したい．入力と出力は以下の通り
#イメージとして1桁ごとにリストに値を入れているかんじ

'''
入力
1234
出力
1
[[1, 2, 3, 4]]
'''




'''
word_list= input().split(" ")
print(word_list[0])
"連続文字列の入力"
"qw er ty とかの入力に使う"
"入力すると空白で区切ったところでlistの番号が与えられる"
'''



'''
A, B, C=stdin.readline().rstrip().split()#何個でもいけることが多い
print(A)
"リストではなく独立したstr型を入れるなら以下のやり方でOK"
'''


#a= stdin.readline().rstrip()
#print(a.upper())
"aという変数に入っているものを大文字にして出力"




#なんかうまく入力されるけど
#a=[[int(i) for i in 1.strip()]for 1 in sys.stdin]
#a = [[int(c) for c in l.strip()] for l in sys.stdin]]
#print(a)
#複数行の数値を入力して正方行列を作成
