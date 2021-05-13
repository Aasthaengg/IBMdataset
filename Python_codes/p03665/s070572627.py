n, p = map(int,input().split())
a=list(map(int, input().split()))
odd=0
even=0
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1

o_pattern=0
for i in range(p,odd+1,2):
    o_pattern += cmb(odd,i)

e_pattern=0
for i in range(even+1):
    e_pattern += cmb(even,i)

print(o_pattern*e_pattern)