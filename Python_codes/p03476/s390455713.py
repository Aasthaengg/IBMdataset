import math

Q = int(input())

def prime(n):
	if n > 1:
		for i in range(2,math.floor(math.sqrt(n))+1):
			if (n % i) == 0:
				return(False)
				break
		else:
			return(True)
	else:
		return(False)

Numero = [0]*100001
for i in range (1, 50001):
	if prime(2*i+1) == 1 and prime(i+1) == 1:
		for j in range (2*i+1, 100001):
			Numero[j]+=1
	else:
		continue

for i in range (0, Q):
	A, B = map(int, input().split())
	print(Numero[B]-Numero[A-1])