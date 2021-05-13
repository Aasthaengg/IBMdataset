def prime_factor(n):
    arr = []
    temp = n
    for i in range(2, 3):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


try:
    from math import gcd
except ImportError:
    from fractions import gcd

n, m = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

n = 1
c = prime_factor(A[0])[0][1]
for a in A:
    if c != prime_factor(a)[0][1]:
        print(0)
        exit()
    n = (n*a)//gcd(n, a)

n //= 2

if n > m:
    ans = 0
else:
    ans = m//n
    ans = (ans+1)//2

print(ans)
