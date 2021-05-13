import sys,math,collections,itertools
input = sys.stdin.readline

N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
cd = A[0]
for a in A:
    cd = math.gcd(cd,a)
if K<=max(A) and K%cd == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
