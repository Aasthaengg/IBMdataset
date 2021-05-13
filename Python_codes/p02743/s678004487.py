
#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	a, b, c = getlist()
	if c - a - b > 0 and (c - a - b) ** 2 - 4 * a * b > 0:
		print("Yes")
	else:
		print("No")


if __name__ == '__main__':
	main()