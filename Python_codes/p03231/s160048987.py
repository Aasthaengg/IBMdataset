def make_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n//i)
    return divisors

N,M = (int(x) for x in input().split())
S = list(input())
T = list(input())
if M > N:
    N,M = M,N
    S,T = T,S
dn = make_divisors(N)
dm = make_divisors(M)
dnm = dn & dm
if dnm == {1}:
    if S[0] == T[0]:
        print(N*M)
    else:
        print('-1')
else:
    gcd = max(dnm)
    n = N // gcd
    m = M // gcd
    for i in range(N//n):
        if S[n*i] != T[m*i]:
            print('-1')
            break
    else:
        print(N*M//gcd)