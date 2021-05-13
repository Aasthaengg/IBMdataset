import math
import heapq
import sys
from collections import Counter

#N,K=map(int, input[].split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
#x=list(map(int, input[].split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

A,B,C=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

if A+B<C:
    print(B+(A+B+1))
else:
    print(B+C)