from math import factorial as fact
import math
import sys
from itertools import product
import numpy as np
from collections import Counter
import datetime
from collections import deque
from bisect import bisect_left, bisect_right
import heapq



#入力:N(int:整数)
def input1():
	return int(input())

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

def swap(a,b):
	tmp=a
	a=b
	b=tmp
	return a,b

H,W,K=input2()
c=[list(input()) for _ in range(H)]

ans=0

for row_line in product(range(2),repeat=H): #[行]0:そのまま，1:赤く塗る
	for col_line in product(range(2), repeat=W): #[列]0:そのまま，1:赤く塗る
		# 黒("#")の数え上げ
		cnt=0
		for row in range(H):
			for col in range(W):
				if c[row][col]=="#" and row_line[row]==0 and col_line[col]==0:
					cnt+=1

		if cnt==K:
			ans+=1
print(ans)





