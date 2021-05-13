MOD = 1000000007
N = int(input())
S = list(map(str, input()))
S = list(map(str, input()))
lst = [0]
i = 0
ans = 1
while i < N:
	if i == N - 1:
		lst.append(1)
		break
	if S[i] == S[i + 1]:
		lst.append(2)
		i += 2
	else:
		lst.append(1)
		i += 1
		

for i in range(len(lst) - 1):
	cur = lst[i]
	nxt = lst[i + 1]
	if cur == 0:
		if nxt == 1:
			ans *= 3
			ans %= MOD
		else:
			ans *= 6
			ans %= MOD
	elif cur == 1:
		if nxt == 1:
			ans *= 2
			ans %= MOD
		else:
			ans *= 2
			ans %= MOD
	else:
		if nxt == 1:
			ans *= 1
		else:
			ans *= 3
			ans %= MOD
			
print(ans)