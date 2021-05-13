#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, M = getlist()
	x = getlist()
	y = getlist()
	X = 0
	Y = 0
	for i in range(N - 1):
		X += ((x[i + 1] - x[i]) * (i + 1) * (N - i - 1)) % con
		X %= con
	for i in range(M - 1):
		Y += ((y[i + 1] - y[i]) * (i + 1) * (M - i - 1)) % con
		Y %= con
	print(X * Y % con)


if __name__ == '__main__':
	main()