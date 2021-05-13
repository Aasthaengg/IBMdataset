import math 
x, n = list(map(float, input().split()))
#print(x,n)
#print(n*x)
n = round(100*n)
print(int(x)*n//100)