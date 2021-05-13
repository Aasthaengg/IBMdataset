N, X = map(int, input().split())
S = list(map(int, input().split()))
l = len(S)

ans = 1
num = 0

for i in range(l):
	num += S[i]
	if num <= X:
		ans += 1

print(ans)