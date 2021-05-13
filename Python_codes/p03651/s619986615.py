from fractions import gcd

N,K = map(int,input().split())
A = [int(i) for i in input().split()]

if K > max(A):
    print('IMPOSSIBLE')
    exit()


a = 0
for i in range(N):
    a = gcd(a,A[i])

if K % a == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
