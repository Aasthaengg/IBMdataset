N, M = map(int, input().split())
A = list(map(int, input().split()))

from math import gcd
def lcm(x, y):
    return x * y // gcd(x, y)

def f(n):
    cnt = 0
    while n:
        if n % 2 == 0:
            n //= 2
            cnt += 1
        else:
            break
    return cnt

l = A[0]//2
cnt = f(l)

for k in range(1, N):
    a = A[k]//2
    c = f(a)
    if cnt != c:
        print(0)
        exit()
    l = lcm(l, a)

print((M // l + 1) // 2)
