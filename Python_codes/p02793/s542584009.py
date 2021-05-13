N = int(input())
A = [int(x) for x in input().split()]

def gcd(p,q):
    if q == 0:
        return p
    else:
        return gcd(q,min(p%q,q-p%q))

if N != 1:
    lcm = 1
    for i in range(N-1):
        if i == 0:
            lcm = A[0]*A[1]//gcd(A[0],A[1])
        else:
            lcm = lcm*A[i+1]//gcd(lcm,A[i+1])

    ans = 0
    for i in range(N):
        ans += lcm//A[i]

    print(ans%(10**9+7))

else:
    print(1)