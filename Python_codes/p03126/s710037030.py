#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm
import collections as C

#N = int(input())
N,M= map(int,input().split())
#P = list(map(int,input().split()))

#S= str(input())
#prod = functools.partial(functools.reduce, operator.mul)
#c=np.array(A)
#p=np.prod(A)

num=[0 for x in range(31)]
for i in range(N):

    K = list(map(int,input().split()))
    for j in K[1:]:
        num[j]+=1
c=0
for k in num:
    if k==N:
        c+=1
print(c)
