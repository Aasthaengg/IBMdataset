import math , sys 
from collections import deque

N = int( input() )
Cs = list( map( int , input().split() ))
Cs.sort(reverse=True)

ans = Cs.pop(0)
i = 1
Q  = (N-2)//2
R = (N-2) % 2
ans += sum([Cs[i]*2 for i in range(Q)])
if R==1:
    ans+=Cs[Q]
print(ans)
