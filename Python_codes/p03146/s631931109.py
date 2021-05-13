s = int(input())

# 3 million should do for upper limit...
K = [0]*3000000

for i in range (0, 10000000):
	if K[s] == 0:
		K[s]=1
		if s%2 == 0:
			s = int(s/2)
		else:
			s = 3*s+1
	else:
		print(i+1)
		exit()