#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	A = []
	for i in range(N):
		a = int(input())
		A.append(a)

	if A[0] != 0:
		print(-1)
	else:
		judge = "Yes"
		ans = 0
		for i in range(N - 1):
			if A[-1 - i] == A[-2 - i] + 1:
				ans += 1
			elif A[-1 - i] <= A[-2 - i]:
				if A[-1 - i] <= N - 1 - i:
					ans += A[-1 - i]
				else:
					judge = "No"
					break
			else:
				judge = "No"
				break
		if judge == "No":
			print(-1)
		else:
			print(ans)

if __name__ == '__main__':
	main()