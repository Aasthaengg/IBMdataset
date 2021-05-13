import math

def func(a,b,x):
	return math.floor(a*x/b)-a*math.floor(x/b)

A,B,N = map(int,input().split())

print(func(A,B,min([B-1,N])))