#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	print(0, flush=True)
	s = input()
	if s != "Vacant":
		left = 0
		leftM = s
		print(N - 1, flush=True)
		s = input()
		if s != "Vacant":
			right = N - 1
			rightM = s
			while True:
				mid = (left + right) // 2
				print(mid, flush=True)
				s = input()
				if s == "Vacant":
					break
				elif (mid - left) % 2 == 0 and s != leftM or (mid - left) % 2 != 0 and s == leftM:
					right = mid
					rightM = s
				else:
					left = mid
					leftM = s

if __name__ == '__main__':
	main()