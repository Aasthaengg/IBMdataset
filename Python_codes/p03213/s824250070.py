
def primesbelow(N):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input N>=6, Returns a list of primes, 2 <= p < N """
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve = [True] * (N // 3)
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

n=int(input())
primes=primesbelow(n+10)
factor={}

def val(n,d):
    ans=0
    t=d
    while(t<=n):
        ans+=(n//t)
        t*=d
    return ans
g2=0
g4=0
g24=0
g14=0
g74=0
for i in primes:
    k=val(n,i)
    if k>=4:
        g4+=1
    if k>=2:
        g2+=1
    if k>=24:
        g24+=1
    if k>=14:
        g14+=1
    if k>=74:
        g74+=1

a=(g2-2)*((g4*(g4-1))//2)
b=g24*(g2-1)
c=g14*(g4-1)
d=g74
print(a+b+c+d)