N = int(input())
A = list(map(int, input().split()))
count = 0

B = [0]*100001

for i in range (0, N):
	if A[i] <= 100000:
		B[A[i]]+=1
	else:
		count+=1

for i in range (1, 100001):
	if B[i] < i:
		count+=B[i]
	if B[i] > i:
		count+=(B[i]-i)

print(count)