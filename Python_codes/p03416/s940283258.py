#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm
#import collections as C #most_common
#import math


#N = int(input())
N,K= map(int,input().split())
#P = list(map(int,input().split()))
#S= str(input())
c=0
for i in range(N,K+1):
    i=list(str(i))
    j=list(reversed(i))
    if i==j:
        c+=1
print(c)
