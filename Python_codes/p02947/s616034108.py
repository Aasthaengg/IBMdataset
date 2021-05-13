N = int(input())
S = []
for _ in range(N):
	t = ''.join(sorted(input()))
	S.append(t)
SS = sorted(S)
ans = 0
t = 0
import math
for i in range(1, N):
	if SS[i - 1] == SS[i]:
		t += 1
		ans += t
	else:
		t = 0
print(ans)
