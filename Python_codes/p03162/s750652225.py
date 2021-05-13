from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
n=int(input())
prev=0
l=[]
for i in range(n):
	l.append(list(map(int,input().split())))
z=[[0,0,0] for i in range(n)]
z[0]=l[0]
for i in range(1,n):
	z[i][0]=l[i][0]+max(z[i-1][1],z[i-1][2])
	z[i][2]=l[i][2]+max(z[i-1][1],z[i-1][0])
	z[i][1]=l[i][1]+max(z[i-1][0],z[i-1][2])
print(max(z[-1]))