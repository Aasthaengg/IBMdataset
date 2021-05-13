# this is the third task 
from collections import defaultdict
N=int(input())
n=1
s=3
brkLoop=False
while True :
    r=(s)**2-(1)-(1)-(n)
    if ( r >= N ):
        break;  
    else:
        n=n+1   
        s=s+1
out=defaultdict(list)
for (x,y,z) in tuple((i,j,k) for i in range(1, n+1) for j in range (1,n+1) for k in range(1,n+1)):
    r=(x+y+z)**2-(x*y)-(y*z)-(x*z)
    if ( r <= N ):
        out[r].append((x,y,z))
for i in range(1,N+1):
    if ( i in out):
        print (len(out[i]))
    else:
        print(0)

