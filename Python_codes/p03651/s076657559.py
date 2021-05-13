N,K=list(map(int,input().split()))
l=list(map(int,input().split()))
import math
if N==1:
   if l[0]==K:
      print("POSSIBLE")
      exit()
   else:
      print("IMPOSSIBLE")
      exit()
A=math.gcd(l[0],l[1])
if K<=max(l):
   for i in range(max(0,N-2)):
      A=math.gcd(A,l[i+2])
   if K%A==0:
      print("POSSIBLE")
   else:
      print("IMPOSSIBLE")
else:
   print("IMPOSSIBLE")