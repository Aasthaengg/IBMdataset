N, M = map(int, input().split())
L = list(map(int, input().split()))

if N == 1:
	if L[0]%M == 0:
		print(1)
		exit()
	else:
		print(0)
		exit()

for i in range (0, N):
	L[i] = L[i]%M

count = 0

for i in range (1, N):
	L[i]= (L[i-1]+L[i])%M

L = sorted(L)

alreadythere = []
import collections

cnt = collections.Counter()
for number in L:
	cnt[number] += 1

L = set(L)

for i in L:
	if i == 0:
		K = cnt[i]
		count+=(int(K*(K-1)/2)+K)
	else:
		K = cnt[i]
		count+=int(K*(K-1)/2)

print(count)