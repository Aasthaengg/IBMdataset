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
	N, K = getlist()
	A = getlist()
	if K == 0:
		print(sum(A))
		sys.exit()	
	dp = [0] * 41
	j = 0
	while True:
		if K % 2 == 1:
			dp[-1 - j] = 1
		K = K // 2
		if K == 0:
			break
		j += 1
	#print(dp)

	p1 = [0] * 41
	p0 = [N] * 41
	for i in range(N):
		a = A[i]
		j = 0
		while True:
			if a % 2 == 1:
				p1[-1 - j] += 1
			a = a // 2
			if a == 0:
				break
			j += 1
	for i in range(41):
		p0[i] -= p1[i]
	#print(p1)
	#print(p0)

	#DP
	DP0 = [0] * 41
	DP1 = [0] * 41
	s = dp.index(1)
	DP0[0] = (2 ** 40) * p1[0]
	DP1[0] = (2 ** 40) * p1[0]
	for i in range(1, s):
		DP0[i] += DP0[i - 1] + (2 ** (40 - i)) * p1[i]
		DP1[i] += DP1[i - 1] + (2 ** (40 - i)) * p1[i]
	if s != 0:
		DP0[s] = DP0[s - 1] + (2 ** (40 - s)) * p0[s]
		DP1[s] = DP1[s - 1] + (2 ** (40 - s)) * p1[s]
	else:
		DP0[s] = (2 ** (40 - s)) * p0[s]
		DP1[s] = (2 ** (40 - s)) * p1[s]
	for i in range(s + 1, 41):
		if dp[i] == 1:
			DP0[i] = DP0[i - 1] + (2 ** (40 - i)) * p0[i]
			DP1[i] = max(DP1[i - 1] + (2 ** (40 - i)) * max(p0[i], p1[i]), DP0[i - 1] + (2 ** (40 - i)) * p1[i])
		else:
			DP0[i] = DP0[i - 1] + (2 ** (40 - i)) * p1[i]
			DP1[i] = DP1[i - 1] + (2 ** (40 - i)) * max(p0[i], p1[i])
	# print(DP0)
	# print(DP1)
	print(max(DP0[-1], DP1[-1]))

if __name__ == '__main__':
	main()