from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=998244353
########################################################
n=int(input())
A=[]
for i in range(n):
    x,y=INPUT()
    a=x+y
    b=y-x
    A.append([a,b])
A.sort()
ans=0
maxiy=A[0][1]
miniy=maxiy
for i in range(n):
    ans=max(max(abs(A[i][0]-A[0][0]),max(abs(A[i][1]-maxiy),abs(A[i][1]-miniy))),ans)
    maxiy=max(maxiy,A[i][1])
    miniy=min(miniy,A[i][1])
print(ans)
