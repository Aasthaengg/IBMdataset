N = int(input())
a = int(N**(1/2))
b = int(N**(1/2))

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

c = prime_factorize(N)
if c[-1] > 10**6:
    print(c[-1] + N//c[-1] - 2)
    exit()

while 1:
    if a*b < N:
        a += 1
    elif a*b > N:
        b -= 1
    else:
        print(a+b-2)
        exit()