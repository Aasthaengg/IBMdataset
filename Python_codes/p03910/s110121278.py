N = int(input())
s = 0
j = 1
for i in range(1, N+1):
	s += i
	if s >= N:
		j = i
		break
k = s - N
for i in range(1, j+1):
	if i == k: continue
	print(i)