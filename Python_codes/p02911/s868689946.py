from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
###############################################################################\
n,k,q=INPUT()
A=[0]*(n+1)
for i in range(q):
    x=int(input())
    A[x]+=1
for i in range(1,n+1):
    if k-q+A[i]>0:
        print("Yes")
    else:
        print("No")
        
