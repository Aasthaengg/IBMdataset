import itertools
import decimal
import math
import collections
import sys
input = sys.stdin.readline

N=int(input())

ListV=list(map(int,input().split()))
ListC=list(map(int,input().split()))

ans=0

for i in range(N):
    if(ListV[i]>ListC[i]):
        ans=ans+ListV[i]-ListC[i]

print(ans)