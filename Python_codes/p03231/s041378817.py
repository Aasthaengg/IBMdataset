n, m = map(int, input().split())
s, t = [input() for i in range(2)]

def gcd(a, b):
    if a < b:
        a, b = b, a
    while(a%b!=0):
        a, b = b, a%b
    return b

a = len(s)
b = len(t)

g = gcd(a, b)

if all([s[a*i//g]==t[b*i//g] for i in range(g)]):
    print(a*b//g)
else:
    print(-1)