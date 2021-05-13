S = input()
w = int(input())

N = len(S)

ans = ''
for i in range(0, N, w):
	ans += S[i]
print(ans)