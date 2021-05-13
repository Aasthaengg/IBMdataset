R,G,B,N = map(int,input().split())
count = 0
for i in range(3001):
	for j in range (3001):
		if i*R+j*G<=N:
			tmp = N-(i*R+j*G)
			if tmp % B == 0:
				count += 1
print(count)
