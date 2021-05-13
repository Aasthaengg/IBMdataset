from math import gcd # Python3.6以降
# --------------------------------------------------------------

# n以下の素数列挙: O-nlogn
def primes(n):
    prs = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            prs.append(i)
    return prs

n    = int(input())
lis  = list(map(int,input().split()))
A    = 10**6
nlis = [0]*A
flg_pairwise = True

for i in range(n):
    nlis[lis[i]-1] += 1

for i in primes(A):
    cnt = 0
    for j in range(i-1,A,i):
        cnt += nlis[j]
    if cnt > 1:
        flg_pairwise = False
        break

if flg_pairwise:
    print('pairwise coprime')
else:
    for i in range(n-1):
        if i==0:
            tmp = gcd(lis[i],lis[i+1])
        else:
            tmp = gcd(tmp,lis[i+1])

    if tmp==1:
        print('setwise coprime')
    else:
        print('not coprime')