import math
A,B,C,D=map(int,input().split())
res = B-A+1
mid = 0
cd = C * D // math.gcd(C, D)
miniNumC = A//C
if A%C==0:
  miniNumC += -1
miniNumD = A//D
if A%D==0:
  miniNumD += -1
maxNumC = B//C
maxNumD = B//D
miniNumCD = A//cd
maxNumCD = B//cd
if A%cd==0:
  miniNumCD += -1
mid += maxNumC -miniNumC + maxNumD -miniNumD -maxNumCD +miniNumCD 
print(res-mid)