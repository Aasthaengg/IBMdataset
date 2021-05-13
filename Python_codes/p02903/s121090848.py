#設定
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

#ライブラリインポート
from collections import deque
import bisect
from heapq import heappop,heappush
from fractions import gcd
from copy import deepcopy

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	H, W, A, B = getlist()
	for i in range(B):
		print("0" * A + "1" * (W - A))
	for i in range(H - B):
		print("1" * A + "0" * (W - A))


if __name__ == '__main__':
	main()