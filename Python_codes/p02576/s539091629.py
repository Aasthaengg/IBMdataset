N, X, T = map(int, input().split())
 
if N % X != 0:
	time = ((N // X) + 1) * T
else:
  time = int(N / X) * T
  
print(time)