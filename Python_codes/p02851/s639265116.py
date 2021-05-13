#ライブラリインポート
from collections import defaultdict

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, K = getlist()
	A = getlist()
	for i in range(N):
		A[i] -= 1

	B = [0]
	for i in range(N):
		B.append(B[-1] + A[i])
	for i in range(N + 1):
		B[i] %= K

	ans = 0
	D = defaultdict(int)
	x = min(N + 1, K)
	for i in range(x):
		ans += D[B[i]]
		D[B[i]] += 1
	for i in range(x, N + 1):
		D[B[i - K]] -= 1
		ans += D[B[i]]
		D[B[i]] += 1
	print(ans)

if __name__ == '__main__':
	main()