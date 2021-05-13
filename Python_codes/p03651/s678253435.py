from fractions import gcd
n,k=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
if k>A[-1]:
    print('IMPOSSIBLE')
else:
    a=A[0]
    for i in range(n):
        a=gcd(a,A[i])
    if a==1:
        print('POSSIBLE')
    else:
        if k%a==0:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')