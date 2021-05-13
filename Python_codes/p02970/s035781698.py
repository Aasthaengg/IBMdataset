import math
N,D=map(int,input().split())
leave=N-2*(2*D+1)
if N<=2*D+1:
    print(1)
else:
    print(math.ceil(leave/(2*D+1))+2)