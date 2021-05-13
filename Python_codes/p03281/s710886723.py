N = int(input())
L = [0]*201

for i in range (1, 201):
	for j in range (i, 201):
		if j%i==0:
			L[j]+=1
            
count = 0

for i in range (1, N+1):
	if i%2 == 1 and L[i] == 8:
		count+=1

print(count)