N,K=map(int,input().split())
A = list(map(int,input().split()))
table = [0]*200001
ans = N
for i in range(N):
	table[A[i]] += 1
table.sort(reverse=True)
for i in range(K):
	ans -= table[i]
print(ans)

