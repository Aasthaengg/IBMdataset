Q=int(input())

def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

nmax = 10**5+1
like = [False]*nmax
for n in range(1,nmax,2):
    if isprime(n) and isprime((n+1)//2):
        like[n]=True

rui = [0]*nmax
rui[0]=int(like[0])
for i in range(1,nmax):
    rui[i] = rui[i-1]+like[i]

for i in range(Q):
    l,r = map(int,input().split())
    print(rui[r]-rui[l-1])