import math , sys

N = int( input() )
A = list( map( int, input().split() ))
A.sort()
Cs = [0 for _ in range(10**6+1)]
M = A[-1]
#print(A)
i=0
M = max(A)
for i in range(N):
    e = A[i]
    if Cs[e]==1:
        Cs[e]=2
    elif Cs[e]==0:
        Cs[e]=1

for i in range(len(Cs)):
    Cs[i] = Cs[i]%2

for e in A:
    i = 2
    while e*i <= M:
        Cs[e*i] = 0
        i+=1
ans = sum(Cs)
print(ans)
