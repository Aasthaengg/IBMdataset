N = int(input())
t = 1

while t*(t+1) < N*2:
	t += 1
x = t*(t+1)//2-N

for i in range(t):
	if t-i <= x:
		x -= t-i
	else:
		print(t-i)