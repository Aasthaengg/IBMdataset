#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	K = int(input())

	div = [] #約数のリスト
	#場合分け
	if ((K ** 0.5) // 1) ** 2 == K:
		n = int((K ** 0.5) // 1)
		for i in range(1, n):
			if K % i == 0:
				div.append(i)
		d = len(div)
		for i in range(d):
			div.append(K // div[i])
		div.append(int((K ** 0.5) // 1))

	else:
		n = int((K ** 0.5) // 1)
		for i in range(1, n + 1):
			if K % i == 0:
				div.append(i)
		d = len(div)
		for i in range(d):
			div.append(K // div[i])

	# print(div)
	ans = 0
	for i in div:
		if i == 1:
			continue
		N = K
		while True:
			if N % i == 0:
				N = int(N // i)
			else:
				if N % i == 1:
					ans += 1
				break

	K = K - 1
	if ((K ** 0.5) // 1) ** 2 == K:
		n = int((K ** 0.5) // 1)
		for i in range(1, n):
			if K % i == 0:
				ans += 2
		ans += 1

	else:
		n = int((K ** 0.5) // 1)
		for i in range(1, n + 1):
			if K % i == 0:
				ans += 2

	print(ans - 1)



if __name__ == '__main__':
	main()