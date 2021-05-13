import math
import heapq
import sys
from collections import Counter

#N,K=map(int, input[0].split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
#x=list(map(int, input[1].split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

N=int(input())
a=list(map(int,input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

cnt=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        a[i+1]=-1
        cnt+=1
        #print(a)


print(cnt)
