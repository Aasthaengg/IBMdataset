N, P = map(int, input().split())
A = [int(i)&1 for i in input().split()]
o = A.count(1)
e = N-o
on = en = 0
def ncr(n, r):
    r = min(r,n-r)
    res=1
    d=1
    for i in range(r):
        res*=n-i
        d *= i + 1
    return res//d

for r in range(e+1):
    en+=ncr(e,r)
for r in range(P, o+1, 2):
    on+=ncr(o,r)

print(on*en)