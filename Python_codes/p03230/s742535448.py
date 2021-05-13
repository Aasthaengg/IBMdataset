import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	M = 0
	for i in range(2, 10 ** 3):
		if i * (i - 1) == 2 * N:
			M = i - 1
			break

	if M == 0:
		print("No")
		return

	print("Yes")
	print(M + 1)

	L = []
	cnt = 1
	for i in range(M):
		l = []
		for j in range(i + 1):
			l.append(cnt)
			cnt += 1
		L.append(l)


	ans = [M]
	for i in range(M):
		ans.append(L[i][-1])
	print(*ans)

	for i in range(M):
		ans = [M]
		for j in range(i + 1):
			ans.append(L[i][j])
		for j in range(i + 1, M):
			ans.append(L[j][i])
		print(*ans)


if __name__ == '__main__':
	main()