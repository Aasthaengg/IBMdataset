mod = 10**9+7
N = int(input())
A = [int(i) for i in input().split()]
if N % 2 == 1:
    import collections
    c = collections.Counter(A)
    for i in range(N):
        if i % 2 == 1:
            continue
        if i == 0:
            if c[i] != 1:
                print(0)
                exit()
        else:
            if c[i] != 2:
                print(0)
                exit()
if N % 2 == 0:
    import collections
    c = collections.Counter(A)
    for i in range(1,N):
        if i % 2 == 0:
            continue
        if c[i] != 2:
            print(0)
            exit()
def pow_k(a,n,mod):
    if n == 0:
        return 1
    if n % 2 ==0:
        return pow_k(a*a % mod,n//2,mod)
    else:
        return a * pow_k(a,n-1,mod) % mod
if N % 2 == 1:
    N -=1
print(pow_k(2,N//2,mod))