from fractions import gcd

N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print('1')
else:
    g = gcd(A[0],A[1])
    lcm = (A[0]*A[1]) // g
    for x in A[2:]:
        lcm = (lcm * x) // gcd(lcm,x)
    print(sum((lcm//x) for x in A)%1000000007)