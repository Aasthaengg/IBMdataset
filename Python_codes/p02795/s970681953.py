#import math
#import collections
#n,k = map(int, input().split( ))
#A = list(map(int, input().split( )))
h = int(input())
w = int(input())
N = int(input())

m = max(h,w)
d = N//m
if N%m == 0:
  print(d)
else:
  print(d+1)