import sys
input = sys.stdin.readline

# A - Digits Sum
def digits_sum(num):
	sum = 0
	
	for s in str(num):
		sum += int(s)
	
	return sum


N = int(input())
ans = sys.maxsize

if N < 10:
	max_index = N
else:
	max_index = N // 2

for A in range(1, max_index):
	B = N - A
	sum = digits_sum(A) + digits_sum(B)
	ans = min(ans, sum)
	
print(ans)