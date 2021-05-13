# C - Bugged
N = int(input())
S = [int(input()) for _ in range(N)]
S = sorted(S)

ans = sum(S)

if ans % 10 != 0:
	pass
else:
	for i in range(N):
		if S[i] % 10 != 0:
			ans = ans - S[i]
			break
	else:
		ans = 0

print(ans)
