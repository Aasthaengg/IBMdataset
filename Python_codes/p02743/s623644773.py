# your code goes here
import math
a,b,c=map(int,input().split(' '))
k=c-a-b
if(k>0 and k*k>4*a*b):
	print("Yes")
	
else:
	print("No")