import math
N=int(input())
C=list(map(int,input().split()))
ave = sum(C) / len(C)
X=math.floor(ave)
Y=X+1
Xsum,Ysum=0,0
for i in range(len(C)):
  Xsum += (C[i]-X)**2
  Ysum += (C[i]-Y)**2
print(min([Xsum,Ysum]))