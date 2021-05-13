from math import sqrt
from itertools import combinations
n = int(input())
a = int(sqrt(2*n))
if n-a*(a+1)//2: print("No")
else:
	print("Yes")
	print(a+1)
	x,y,m = [[str(a)] for i in range(a+1)],[i for i in range(a+1)],1
	for i,j in combinations(y,2):
		x[i].append(str(m))
		x[j].append(str(m))
		m+=1
	for i in x: print(" ".join(i)) 