#import math
import collections
#n,k = map(int, input().split( ))
n = int(input())
A = list(map(int, input().split( )))
c = collections.Counter(A)
s = 0
for a in c:
  if c[a] >= 2:
    s += c[a]*(c[a]-1)//2
#print(s)  
for a in A:
  if c[a] == 1:
    print(s)
  else:
    print(s - c[a] + 1) 