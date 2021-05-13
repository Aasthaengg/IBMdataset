N,M = map(int,input().split())
A = list(map(int,input().split()))

sum = 0
for i in range(N):
	sum = sum + A[i]

boarder = sum /(4 * M)
count = 0
for i in range(N):
	if A[i] >= boarder:
		count = count + 1
if M <= count:
	print("Yes")
else:
	print("No")