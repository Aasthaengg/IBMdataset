N = int(input())
count = 0

import math  
  
# Method to print the divisors 
def printDivisors(n) : 
	list = []  
	for i in range(1, int(math.sqrt(n) + 1)) : 
		if (n % i == 0) : 
			if (n / i == i) : 
				list.append(i) 
			else : 
				list.append(i) 
				list.append(int(n / i)) 
	return(list)

A = printDivisors(N)

for i in range (1, len(A)):
	if N//(A[i]-1) == N/A[i]:
		count+=(A[i]-1)

print(count)