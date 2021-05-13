from sys import stdin
import sys
import math
n,k=list(map(int,(stdin.readline().strip().split())))
w=[int(input()) for x in range(n)]
def f(p):
    i=0
    for j in range(k):
        weight=0
        while(weight+w[i]<=p):
            weight+=w[i]
            i+=1
            if i==n:return n
    return i
left=0
right=10**9+1
mid=right//2
while(True):
    length=f(mid)
    if length==n:
        l=f(mid-1)
        if length==l:
            right=mid
            mid=(right+left)//2
        else:
            print(mid)
            exit()
    if length>n:
        right=mid
        mid=(right+left)//2
    if length<n:
        left=mid
        mid=(right+left)//2
