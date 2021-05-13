N=int(input())
lis=[tuple(map(int,input().split())) for _ in range(N)]
import itertools,math
p = itertools.permutations(list(range(N)))
sm=0

for v in p:
    #print(v)
    for k in range(N-1):
        xi,yi=lis[v[k]]
        xj,yj=lis[v[k+1]]
        #print(xi,yi,xj,yj)
        sm+=((xi-xj)**2+(yi-yj)**2)**(1/2)
print(sm/math.factorial(N))