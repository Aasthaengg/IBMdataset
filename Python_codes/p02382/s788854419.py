import math

Manhattan = 0
Euclid = 0
Three = 0
Chebychev = []
num = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

# ???????????????????????¢
for i in range(num):
	Manhattan += math.fabs(x[i] - y[i]) 
	Euclid += math.fabs((x[i] - y[i])**2)
	Three += math.fabs((x[i] - y[i])**3)
	Chebychev.append(math.fabs((x[i] - y[i])))

print(Manhattan)
print(math.sqrt(Euclid))
print(math.pow(Three,1/3))
print(max(Chebychev))