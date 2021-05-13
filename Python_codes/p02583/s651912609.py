
N = int(input())
Ns = list(map(int, input().split()))
Ns.sort()
ans = 0

for i in range(0, N - 2):
	for j in range(i + 1, N - 1):
		for k in range(j + 1, N):
			if(Ns[i] == Ns[j] or Ns[k] == Ns[j]):
				continue

			if(Ns[i] + Ns[j] > Ns[k] and Ns[j] + Ns[k] > Ns[i] and Ns[k] + Ns[i] > Ns[j]):
				ans += 1
print(ans)