def getlist():
	return list(map(int, input().split()))

#初期化
N, K = getlist()
A = getlist()
S = sum(A)
n = int((S ** 0.5) // 1) + 1
gcd = []
for i in range(1, n):
	if S % i == 0:
		gcd.append(i)
x = len(gcd)
for i in range(x):
	gcd.append(S // gcd[i])
gcd = sorted(gcd)

#計算
ans = 1
for i in gcd:
	P = []
	for j in A:
		x = j % i
		if x != 0:
			P.append([x, i - x])
	P = sorted(P)
	a = 0
	b = 0
	for j in range(len(P)):
		a += P[j][0]
	s = 0
	for j in range(len(P)):
		a -= P[-1 - j][0]
		b += P[-1 - j][1]
		s += P[-1 - j][1]
		if a == b:
			break
	if s <= K:
		ans = i

print(ans)