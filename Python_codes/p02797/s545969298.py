#import collections
import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
A=[]
B=[]
for i in range():
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)'''
#import copy
#import numpy as np

n, k, s = map(int, input().split())
ans = [s+1 if s != 10**9 else 1 for i in range(n)]
#print(ans)
for i in range(k):
    ans[i]=s
for i in ans:
    print(i)
