import sys
input = sys.stdin.readline

def getlist():
	return list(map(int, input().split()))

#初期化
N, C = getlist()
Lis = [[0 for i in range(10 ** 5 + 3)] for j in range(C)]
for i in range(N):
	s, t, c = getlist()
	Lis[c - 1][s] += 1
	Lis[c - 1][t] -= 1

#計算
for j in range(C):
	v = "x"
	for i in range(10 ** 5 + 1):
		if Lis[j][i] == 1:
			v = "o"
			Lis[j][i] = "o"
		elif Lis[j][i] == 0:
			Lis[j][i] = v
		elif Lis[j][i] == -1:
			Lis[j][i] = "o"
			v = "x"

ans = 0
for i in range(10 ** 5 + 1):
	val = 0
	for j in range(C):
		if Lis[j][i] == "o":
			val += 1
	ans = max(ans, val)

print(ans)