N = int(input())
Ns = {}
for i in range(1, N + 1):
	num = i
	cnt = 0
	while num % 2 == 0:
		num //= 2
		cnt += 1
	Ns[i] = cnt
print(max(Ns, key=Ns.get))
