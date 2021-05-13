#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm
#import collections as C #most_common
#import math


#N = int(input())
A,B,C,K= map(int,input().split())
#P = list(map(int,input().split()))
#S= str(input())

if K%2==0:
    ans = A-B
else:
    ans = B-A
    
if ans>10**18:
    print('Unfair')
else:
    print(ans)
