#ABC_085_C_Otoshidama.py
N,Y = list(map(int, input().split()))
x=-1
y=-1
z=-1
for a in range(N+1): #number of 10000yen
	for b in range(N+1-a): #number of 5000yen
		c=N-a-b #number of 1000yen
		sum=10000*a + 5000*b + 1000*c
		if sum == Y:
			x=a
			y=b
			z=c
print(x,y,z)