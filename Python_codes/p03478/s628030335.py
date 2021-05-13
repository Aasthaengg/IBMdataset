# ABC_083_B_Some_Sums
N, A, B = list(map(int, input().split()))

def findSumOfDigits(N):
	sum = 0
	while N > 0:
		sum += N % 10
		N = N//10
	return(sum)
	
total = 0
for i in range(1, N+1):
	sum = findSumOfDigits(i)
	if (A <= sum and sum <= B):
		total += i
print(total)
