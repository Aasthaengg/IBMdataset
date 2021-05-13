n,k = map(int,input().split())

di = 10**9+7
lis = [0 for i in range(n+1)]
lisr = [0 for i in range(n+1)]

lis[0]=1
for i in range(1,n+1):
    lis[i] = (lis[i-1]*i)%di

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (K*x)%di
        x = (x*x)%di
        n //= 2

    return (K * x)%di


lisr[0]=1
for i in range(1,n+1):
    lisr[i] = pow_k(i,di-2)


for i in range(1,n+1):
    lisr[i] = (lisr[i-1]*lisr[i])%di

def comb(i,j):
    tmp = (lis[i]*lisr[i-j])%di
    return (tmp*lisr[j])%di


for i in range(k):
    blu = i+1
    red = blu-1
    if (k-blu)<0 or (n-k-red) < 0:
        print(0)
        continue

    cnt = comb((n-k-red)+blu,blu)
    cnt = (cnt*comb((k-blu)+red,red))%di
    print(cnt)
