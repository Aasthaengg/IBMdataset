n = int(input())

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

li = []

for i in range(1,n+1):
    li += prime_factorize(i)

from collections import Counter

C = Counter(li)

a = 0
b = 0
c = 0
d = 0
e = 0

for i,j in C.items():
    if j >= 74:
        e += 1
    elif 24 <= j < 74:
        d += 1
    elif 14 <= j < 24:
        c += 1
    elif 4 <= j < 14:
        b += 1
    elif 2 <= j < 4:
        a += 1

point = 0

#75
point += e
#25 3
point += (d+e)*(a+b+c)+(d+e-1)*(d+e)
#15 5
point += (c+d+e)*b+(c+d+e-1)*(c+d+e)
#2 5 5
f = b+c+d+e
point += a*f*(f-1)//2+f*(f-1)*(f-2)//2

print(point)