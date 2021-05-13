#設定
import sys
input = sys.stdin.buffer.readline

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, C = getlist()
	left1sum = [0]
	right1sum = [0]
	left2sum = [0]
	right2sum = [0]
	X = []
	V = []
	for i in range(N):
		x, v = getlist()
		X.append(x)
		V.append(v)
	for i in range(N):
		left1sum.append(left1sum[-1] + V[-1 - i])
		left2sum.append(left2sum[-1] + V[-1 - i])
		right1sum.append(right1sum[-1] + V[i])
		right2sum.append(right2sum[-1] + V[i])
	# print(right1sum)
	# print(right2sum)
	# print(left1sum)
	# print(left2sum)
	for i in range(N):
		right1sum[i + 1] -= X[i]
		right2sum[i + 1] -= 2 * X[i]
		left1sum[i + 1] -= C - X[-1 - i]
		left2sum[i + 1] -= 2 * (C - X[-1 - i])

	for i in range(N):
		right1sum[i + 1] = max(right1sum[i + 1], right1sum[i])
		right2sum[i + 1] = max(right2sum[i + 1], right2sum[i])
		left1sum[i + 1] = max(left1sum[i + 1], left1sum[i])
		left2sum[i + 1] = max(left2sum[i + 1], left2sum[i])
	# print(right1sum)
	# print(right2sum)
	# print(left1sum)
	# print(left2sum)
	ans = 0
	for i in range(N + 1):
		ans = max(ans, right1sum[i] + left2sum[N - i])
		ans = max(ans, right2sum[i] + left1sum[N - i])
	print(ans)

if __name__ == '__main__':
	main()