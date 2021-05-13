#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, P = getlist()
	S = list(input())

	#例外処理
	if P == 2:
		ans = 0
		for i in range(N):
			if int(S[i]) % 2 == 0:
				ans += i + 1
		print(ans)
		return

	if P == 5:
		ans = 0
		for i in range(N):
			if int(S[i]) % 5 == 0:
				ans += i + 1
		print(ans)
		return
	
	#計算
	D = defaultdict(int)
	D[0] = 1
	var = 0
	for i in range(N):
		var += pow(10, i, P) * int(S[N - 1 - i])
		var %= P
		D[var] += 1

	ans = 0
	for i in D:
		var = D[i]
		ans += int((var * (var - 1)) // 2)

	print(ans)

if __name__ == '__main__':
	main()