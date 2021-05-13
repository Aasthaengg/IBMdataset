from functools import reduce
N = int(input())
*A, = map(int, input().split())
def gcd(a,b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
ans = reduce(gcd, A)
print(ans)