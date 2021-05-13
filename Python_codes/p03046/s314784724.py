'''input
5 12
'''

N, K = [int(x) for x in input().split()]

if not K:
	for i in range(1 << N):
		print(i, i, end=' ')
	exit()

if N == 1:
	if K == 1:
		print(-1)
		exit()

if K >= 1 << N:
	print(-1)
	exit()

prad = list(range(1 << N))

prad.remove(K)

pab = list(reversed(prad))


for i in prad:
	print(i, end=' ')

print(K, end=' ')
for i in pab:
	print(i, end=' ')
print(K)