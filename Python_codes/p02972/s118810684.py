N = int(input())
A = list(map(int, input().split()))
A = [0] + A
balls = [0] * (N+1)

for i in range(N, 0, -1):
	tmpBalls = 0
	x = 1
	while i * x <= N:
		tmpBalls += balls[i*x]
		x += 1
	
	if A[i] == 1 and tmpBalls % 2 == 1:
		pass
		
	elif A[i] == 1 and tmpBalls % 2 == 0:
		balls[i] += 1
	
	elif A[i] == 0 and tmpBalls % 2 == 1:
		balls[i] += 1
	
	elif A[i] == 0 and tmpBalls % 2 == 0:
		pass
		

isOkay = True
for i in range(1, N+1):
	if balls[i] > 1:
		print(-1)
		exit()
	
print(balls.count(1))	
for i in range(1, N+1):
	if balls[i]:
		print(i)