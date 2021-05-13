# -*- coding: utf-8 -*-
import sys
import itertools#これは色々使える組み込み関数みたいなやつ
import math#数学的計算はこれでいける。普通に0.5乗しても計算可能
#w=input()
i=0
j=0
s=0
eq=''
A,B,C=map(int,input().split())
#A,B,Cを分けて入力しかも一行で
#N=int(input())
#Nori=N
#D, N=input().split()
#S=input()
D=0
D=A+B
if D >=C:
    print('Yes')
    sys.exit()
print('No')
def change(i):
    return int(i)

#S_list=list(S)
numberlist=[]
numberlist=list(map(change, numberlist))
keisanlist=sorted(numberlist, reverse=True)

#M=int(input())
#drink_list = [list(map(int, input().split(" ")))for i in range(M)]
#print(T_list[1])
#D=int(D)
#N=int(N)
#不本意だが内包表記で二次元の空のリストを作成する
     
#dp=[['' for i in range(2)] for j in range(N)]
#absTH=[''for i in range(N)]
#K=int(K)
#S_list=[]
#sentence_list=[]
#total=0
#mojiretu=""
#センテンスを暗記するのではなく、まずinput()を書いて、膨らます感じで記述する。すると#思考の流れ通りに書ける。素晴らしい！
#for i in range(K):
# ID_list.append(i+1)
#print(ID_list)
#for i in range(H)
#この下の行が二次元リストの読み込
#intを消して記号を読み込めるようにしたしかしこれでは文字列から読み込んでいるのと同じ
#weight_value_list =  [list(input())for i in range(N)]#一文字づつばらして入れてしまう
#s = [input() for i in range(N)]
#複数行に複数の入力値を取得し、出力する
#sentence_list =  (list(input())for i in range(N))
#for i in range(H):
#  ppixel_list=list(input())
    
#print(pixel_list)
#high_pixel_list =[['' for i in range(W)]for j in range(2*H)]
#print(high_pixel_list)
#print(pixel_list[0][1])#行　列の順番にかっこが並んでいる
#print(a_list)
first_term=0
second_term=0
#整数二次元配列を読み込む時のやり方
#a_b_c_list =  [list(map(int, input().split(" ")))for i in range(N)]
     
#センテンスを暗記するのではなく、まずinput()を書いて、膨らます感じで記述する。すると#思考の流れ通りに書ける。素晴らしい！
  
     
#x, y = [0]*N, [0]*N#N個の空のリストを作成
#l = list(range(N))#範囲がNのリストを作成する
     
#for i in range(N):
#  x[i], y[i] = map(int, input().split())
#分けて入力する形式を設定することで可読性が高く仕上がっている
#素晴らしいことだ
     
     
distance = 0
#comb = list(itertools.permutations(l))
#prmutation:英語の意味としては順列である
'''p[, r]で
長さrのタプル列、重複なしのあらゆる並びを表す
今回はリストlの重複なしの並び替え順序を新たなリストに収納している
並び方を計算しリストに収納しているイメージ
l[0,1,2]
l[0,2,1]これにもリスト番号が0,1,2と割り振られている
これが全通り入っている
これ作った人はすごい
自分も早く理解したい
'''
#for i in range(0, len(comb)):#i番目のパターンの時を考える。
#  for j in range(0, N-1):#lのリスト番号を読み込み
#    distance += math.sqrt((x[comb[i][j]]-x[comb[i][j+1]])**2 + (y[comb[i][j]]-y[comb[i][j+1]])**2)
'''
各経路の距離を足していき全距離分を経路数
で割れば平均距離が出るので各経路ごとの距離は
不必要と判断されている。
'''
#print(distance/len(comb))
# dp[i+1][j]=max(dp[i][j]+a_b_c_list[i],dp[i][j],dp[i][j])
#リストを一周するようにすればいいのか
