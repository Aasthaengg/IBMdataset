import math
n=int(input())
A=[]
#print(A)
for i in range(2):
	A.append(input().split())

#Manhattan=|x1-y1|+|x2-y2|+|x3-y3|
Manhattan=0
#Euclidean
Euclidean=0
#Minkowski_3
Minkowski_3=0
#Chebyshev
Chebyshev=[]
for i in range(n):	
	a=math.fabs(int(A[0][i])-int(A[1][i]))
	Manhattan+=a
	Euclidean+=a**2
	Minkowski_3+=a**3
	Chebyshev.append(a)




Euclidean=math.sqrt(Euclidean)
Minkowski_3=Minkowski_3**(1/3)
Chebyshev.sort()
Chebyshev.reverse()
print(Manhattan)
print(Euclidean)
print(Minkowski_3)
print(Chebyshev[0])