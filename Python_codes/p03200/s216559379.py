#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm
#import collections

#N = int(input())
#a,b= map(int,input().split())
#P = list(map(int,input().split()))
#B = list(map(int,input().split()))
S= str(input())
#prod = functools.partial(functools.reduce, operator.mul)
#c=np.array(A)
#p=np.prod(A)

w = S.count('W')
b = S.count('B')
c=0
v=0
for i in range(len(S)):
    if S[i]=='B':
        v+=1
        c += (len(S)-b + v) - (i +1)
print(c)
