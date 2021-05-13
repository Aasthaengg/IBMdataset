#設定
import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	L = []
	for i in range(N):
		P = int(input())
		L.append([P, i])
	L = sorted(L)
	ans_pre = 1
	val = 1
	for i in range(N - 1):
		if L[i + 1][1] > L[i][1]:
			val += 1
		else:
			ans_pre = max(ans_pre, val)
			val = 1
	ans_pre = max(ans_pre, val)

	ans = N - ans_pre
	print(N - ans_pre)

if __name__ == '__main__':
	main()