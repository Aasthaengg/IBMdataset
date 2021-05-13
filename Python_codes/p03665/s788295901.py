def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n, p = map(int,input().split())
A = list(map(int,input().split()))

odd = 0
for a in A:
    if a%2:
        odd += 1

all_c = 0
for i in range(n+1):
    all_c += cmb(n, i)

odd_c = 0
for i in range(-(-odd//2)):
    #print(odd,"C",2*i+1)
    odd_c += cmb(odd, 2*i+1)
#print("奇数個の組", odd_c)

even_c = 0
for i in range(n-odd+1):
    even_c += cmb(n-odd, i)

if p == 1:
    print(odd_c*even_c)
else:
    print(all_c - odd_c*even_c)