S = input().rstrip()
N = len(S) - 1
p = "+"

ans = 0
for bit in range(1 << N):
	mae = 0
	for j in range(N):
		if (bit >> j) & 1:
			ans += int(S[mae: j + 1])
			mae = j + 1
	ans += int(S[mae: len(S)])
print(ans)