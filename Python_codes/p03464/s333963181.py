K = int(input())
A = [int(i) for i in input().split()]

N_min = 2
N_max = 2
for a in A[K::-1]:
	if N_min + (a - N_min) % a > N_max:
		print(-1)
		exit(0)
	else:
		# N_min -> smallest # that is # >= prev N_min and # % a == 0
		N_min += (a - N_min) % a
		# N_max -> smallest # that is # >= prev N_max and # % a == a-1
		N_max += (a - N_max - 1) % a
print(N_min, N_max)
