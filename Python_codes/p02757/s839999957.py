N, P = map(int, input().split())
S = input()
 
ans = 0
if P == 2 or P == 5:
	for i in range(N):
		if int(S[i]) % P == 0:
			ans += i+1
else:
	t = [0] * 20000
	t[0] = 1
	now = 0
	po = 1
	for i in range(N):
		n = N - i - 1
		now = (int(S[n]) * po + now) % P
		po = 10 * po % P
		ans += t[now]
		t[now] += 1
print(ans)