from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
n=int(input())
l=list(map(int,input().split()))
z=[float("infinity") for i in range(n)]
z[0]=0
for i in range(n):
	if i<n-1:
		z[i+1]=min(z[i+1],z[i]+abs(l[i]-l[i+1]))
	if i<n-2:
		z[i+2]=min(z[i+2],z[i]+abs(l[i]-l[i+2]))
print(z[-1])