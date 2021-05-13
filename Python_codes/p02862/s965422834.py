X, Y = map(int, input().split())
a = 2*Y-X
b = 2*X-Y

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

if a%3==0 and b%3==0 and a>=0 and b>=0:
    a //= 3 
    b //= 3
    print(combination(a+b, a))
else:
    print(0)