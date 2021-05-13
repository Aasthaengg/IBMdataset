from fractions import gcd
N,K=map(int,input().split(' '))
A=sorted(list(map(int,input().split(' '))))
G=A[0]
for i in A[1:]:
    G=gcd(G,i)
if A[-1] >= K and K%G==0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')