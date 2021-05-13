N=int(input())
C=[0]*6

for _ in range(N):
    C['MARCH'.find(input()[0])]+=1

from itertools import*
D=list(combinations(C[:5],3))

ans=0
for i,j,k in D:
    ans+=i*j*k

print(ans)