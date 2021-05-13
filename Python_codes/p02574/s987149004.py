import math

MAX=10**6+3
table = list(range(MAX))
i=2
n=MAX
while i<n:
    table[i] = 2
    i+=2
p=3
while p*p<=n:
    if table[p]<p:
        p+=2
        continue
    x=p
    while x<=n:
        table[x]=p
        x+=p
    p+=2


def primeFactorSet(n):
    result = set()
    while table[n]!=1:
        result.add(table[n])
        n //= table[n]
    return result
    

n = int(input())
A = list(map(int,input().split()))
pairwise = True
flags = [False for _ in range(MAX)]

for i in range(n):
    a=A[i]
    if pairwise:
        t = primeFactorSet(a)
        for p in t:
            if flags[p]:
                pairwise = False
                break
            flags[p]=True
    if i==0:
        g=a
    else:
        g=math.gcd(g,a)
    
if g>1:
    print("not coprime")
elif pairwise:
    print("pairwise coprime")
else:
    print("setwise coprime")