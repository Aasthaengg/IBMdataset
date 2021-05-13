n,p=map(int,input().split())
a=[i%2 for i in map(int,input().split())]

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

oishii = a.count(1)

c = sum([cmb(oishii,i) for i in range(p,oishii+1,2)])

print(c*2**(n-oishii))
