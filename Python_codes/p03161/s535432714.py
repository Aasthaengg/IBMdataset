from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
n,k=map(int,input().split())
l=list(map(int,input().split()))
z=[float("infinity") for i in range(n)]
z[0]=0
for i in range(n):
	for j in range(1,k+1):
		if i+j<n:
			z[i+j]=min(z[i+j],z[i]+abs(l[i]-l[i+j]))
		else:
			break
print(z[-1])
