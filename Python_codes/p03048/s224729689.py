R, G, B, N = map(int, input().split())

count = 0

for i in range (0, N//R+1):
	for j in range (0, N//G+1):
		if (N-R*i-G*j)>= 0 and (N-R*i-G*j)%B == 0:
			count+=1

print(count)