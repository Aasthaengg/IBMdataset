from fractions import gcd
n,m = [int(x) for x in input().split()]
s = input()
t = input()

def f(n,m):
    return n*m // gcd(n,m)

ans = f(n,m)

if s[::ans//m] == t[::ans//n]:
    print(ans)
else:
    print(-1)