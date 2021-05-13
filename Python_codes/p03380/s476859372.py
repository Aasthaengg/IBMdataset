import bisect
import math
n = int(input())
l = sorted(list(map(int,input().split())))
if len(l)==2 :
  print(l[-1],l[-2])
  exit()
  
a = l[-1]/2
s = bisect.bisect_left(l,a)
if l[s]==a:
  print(l[-1],l[s])
  exit()
k1 = l[s-1]
k2 = l[s]
s1 = a-k1
if k2==l[-1]:
  k2 = k1
s2 = abs(k2-a)
#print(s,k1,k2,s1,s2)
if s1<=s2:
  print(l[-1],k1)
else:
  print(l[-1],k2)