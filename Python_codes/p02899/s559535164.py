N = int(input())
A = list(map(int, input().split()))
result = [0] * N
for i in range(N):
	result[A[i]-1] = str(i+1)
s = ' '.join(result)
print(s)