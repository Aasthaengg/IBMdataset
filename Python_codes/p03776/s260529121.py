import sys
input = sys.stdin.readline
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


n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort()
sm=sum(v[-a:])
av=sm/a
ky=v[-a]
c=v.count(ky)
co=0
for i in range(n):
    if v[-i-1]>ky:
        co+=1
ans=0
#print(v)
if co>0:
    ans=cmb(c,a-co)
else:
    for i in range(a,min(b+1,c+co+1)):
        ans+=cmb(c,i-co)
print(av)
print(ans)
