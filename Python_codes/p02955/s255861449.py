import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

def cost(d,numList):
    r = [x%d for x in numList]
    r.sort(reverse=True)
    p = sum(r)//d
    c = 0
    for i in range(p):
        c += d - r[i]
    return(c)

def divisors(n):
    sq = math.ceil(math.sqrt(n))
    ans = []
    for i in range(1,sq):
        if n%i == 0:
            ans.append(i)
            ans.append(n//i)
    return(ans)

divs = divisors(sum(A))
ans = 1
for d in divs:
    c = cost(d, A)
    if c <= K:
        ans = max(ans,d)
print(ans)