n, m = list(map(int, input().split()))
s = input()
t = input()

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

l = n*m//gcd(n,m)

nd = l//n
md = l//m

common = nd*md//gcd(nd,md)
nc = common//nd
mc = common//md

sol = True
for i in range(0, l, common):
    ind = i//common
    if s[ind * nc] != t[ind * mc]:
        sol = False
        break

print(l if sol else -1)