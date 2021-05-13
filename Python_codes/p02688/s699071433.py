N,K = map(int,input().split())

okasi = [0] * (N + 1)
for i in range(K):
	d = int(input())
	A = list(map(int,input().split()))
	for j in range(d):
		okasi[A[j]] = 1
#print(okasi)

count = 0
for i in range(1,N +1,1):
	if okasi[i] != 1:
		count = count + 1
print(count)