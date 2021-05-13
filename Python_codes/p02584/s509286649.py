from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import math
sys.setrecursionlimit(4100000)
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
input=lambda :sys.stdin.readline().rstrip()



X,K,D=map(int,input().split())

if X<0:
    X*=-1


k=X//D
if k>=K:
    print(X-K*D)
else:
    K-=k
    if K%2:
        print(-(X-(k+1)*D))
    else:
        print(X-k*D)
