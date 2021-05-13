def modinv(a, m):
    b, u, v = m, 1, 0
    while(b):
        a, b, u, v = b, a%b, v, u-(a//b)*v
    return u % m

def modfac(n, m):
    res = [1] * (n+1)
    for i in range(2, n+1):
        res[i] = res[i-1] * i % m
    return res

def modc(n, r, m):
    lst = modfac(n, m)
    return lst[n] * modinv(lst[r], m) * modinv(lst[n-r], m) % m

x, y = map(int, input().split())
if (x+y)%3 == 0 and x >= (x+y)//3 and x <= 2*(x+y)//3:
    print(modc((x+y)//3, x-(x+y)//3, 1000000007))
else:
    print(0)