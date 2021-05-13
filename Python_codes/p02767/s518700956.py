n = int(input())
x = list(map(int,input().split()))
answer = 0

for i in range(min(x),max(x)+1):
	result = 0
	for j in range(n):
		result += (x[j] - i) ** 2
	if answer == 0 or answer > result:
		answer = result
		number = i

print(answer)