import math
import _collections
n=int(input())
A=list(map(int,input().split()))
ans=A[0]
X=[0]*(max(A)+1)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return set(a)



for i in range(1,n):
    ans=math.gcd(ans,A[i])

if ans!=1:
    print('not coprime')
else:
    ans='pairwise coprime'
    for a in A:
        B=prime_factorize(a)
        for b in B:
            if X[b]!=0:
                ans='setwise coprime'
            else:
                X[b]+=1
    print(ans)