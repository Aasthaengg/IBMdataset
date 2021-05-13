from functools import lru_cache

@lru_cache(maxsize=None)

def kaijou(n):
    if n <= 1:
        return 1
    return kaijou(n-1)*n

n,p = map(int,input().split())
even = 0
odd = 0
ans = 0
for i in map(int,input().split()):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if p == 0:
    eveng = 0
    for j in range(0,odd+1,2):
        if j > odd:
            break
        eveng += kaijou(odd)/kaijou(odd-j)/kaijou(j)
    ans = int((2**even)*eveng)
else:
    oddg = 0
    #print(odd)
    for j in range(1,odd+1,2):
        if j > odd:
            break
        oddg += kaijou(odd)/kaijou(odd-j)/kaijou(j)
    ans = int((2**even)*oddg)
print(ans)