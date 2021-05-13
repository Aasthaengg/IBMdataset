a,b,c = list(map(int, input().split()))
answer = 0
for n in range(a, b + 1):
	if(c % n == 0):
		answer += 1
print(answer)