import math
from collections import defaultdict,deque
from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""
t=1
#t=ii()
for _ in range(t):
    n=ii()
    a=ll()
    i=n-1;
    while(i>-1):
        print(a[i],end=" ")
        i-=2
    for i in range(n%2,n,2):
        print(a[i],end=" ")