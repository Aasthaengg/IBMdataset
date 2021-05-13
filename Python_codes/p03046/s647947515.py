#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict
import copy

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	M, K = getlist()
	if M == 0:
		if K == 0:
			print(0, 0)
		else:
			print(-1)
	elif M == 1:
		if K == 0:
			print(0, 0, 1, 1)
		else:
			print(-1)

	else:
		if K >= 2 ** M:
			print(-1)
		else:
			ans = []
			for i in range(2 ** M):
				if i != K:
					ans.append(i)
			ans.append(K)
			for i in range(2 ** M):
				if 2 ** M - 1 - i != K:
					ans.append(2 ** M - 1 - i)
			ans.append(K)
			print(" ".join(list(map(str, ans))))

if __name__ == '__main__':
	main()