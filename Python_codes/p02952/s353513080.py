import sys    #インタプリタや実行環境に関する情報を扱うためのライブラリ
import os     #フォルダやファイルを操作
import math

N=int(input())
count=0

for i in range(N+1):
    if i==0:
        continue
    if i<10:
        count +=1
    if i<100:
        continue
    elif i<1000:
        count +=1
    elif i<10000:
        continue
    elif i<100000:
        count+=1

print(count)