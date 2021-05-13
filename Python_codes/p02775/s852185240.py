# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
import collections
import copy
import heapq
from collections import defaultdict
from heapq import heappop, heappush
import itertools
input = sys.stdin.readline

##### リストの 二分木検索 #####
# bisect_left(lists, 3)
# bisect_right(lists, 3)

##### プライオリティキュー #####
# heapq.heapify(a) #リストaのheap化
# heapq.heappush(a,x) #heap化されたリストaに要素xを追加
# heapq.heappop(a) #heap化されたリストaから最小値を削除＆その最小値を出力

# heapq.heappush(a, -x) #最大値を取り出す時は、pushする時にマイナスにして入れよう
# heapq.heappop(a) * (-1) #取り出す時は、-1を掛けて取り出すこと

##### タプルリストのソート #####
# sorted(ans) #(a, b) -> 1st : aの昇順, 2nd : bの昇順
# sorted(SP, key=lambda x:(x[0],-x[1])) #(a, b) -> 1st : aの昇順, 2nd : bの降順
# sorted(SP, key=lambda x:(-x[0],x[1])) #(a, b) -> 1st : aの降順, 2nd : bの昇順
# sorted(SP, key=lambda x:(-x[0],-x[1])) #(a, b) -> 1st : aの降順, 2nd : bの降順

# sorted(SP, key=lambda x:(x[1])) #(a, b) -> 1st : bの昇順
# sorted(SP, key=lambda x:(-x[1])) #(a, b) -> 1st : bの降順

##### 無限 #####
# inf = float('inf')

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))

inf = float('inf')

def main():
	N = input()
	N = N[:-1]
	N = "0" + N
	N = N[::-1]

	dp = [[inf,inf] for i in range(len(N)+2)]
	dp[0][0] = 0
	#print(dp)

	cnt = 0
	for ii in N:
		i = int(ii)
		cnt += 1
		#print(dp)
		for j in range(10):
			if i > j:
				tmp = j + 10 - i
				dp[cnt][1] = min(dp[cnt][1], dp[cnt-1][0] + tmp + j)
			else:
				tmp = j - i
				dp[cnt][0] = min(dp[cnt][0], dp[cnt-1][0] + tmp + j)

			tmptmp = j-1
			if i > tmptmp:
				tmp = tmptmp + 10 - i
				dp[cnt][1] = min(dp[cnt][1], dp[cnt-1][1] + tmp + j)
			else:
				tmp = tmptmp - i
				dp[cnt][0] = min(dp[cnt][0], dp[cnt-1][1] + tmp + j)

	#print(dp)
	print(dp[len(N)][0])

if __name__ == "__main__":
	main()
