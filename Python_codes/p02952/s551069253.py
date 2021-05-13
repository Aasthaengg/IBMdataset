n = int(input())

def d(k):
    s = 0
    while k > 0:
        k //= 10
        s += 1
    return s

dn = d(n)
a = 0
for i in range(1, dn + 1):
    if i % 2 == 1:
        if n < 10 ** i:
            a += n - 10**(i- 1) + 1
        else:
            a += 10 ** i - 10 ** (i - 1)
print(a)