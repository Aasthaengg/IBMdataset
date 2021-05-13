import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n=int(input())
l=[0]*(n+1)
for i in range(1,n+1):
    c=prime_factorize(i)
    #print(c)
    for j in range(len(c)):
        l[c[j]]+=1
#print(l)
ans=1
for i in range(n+1):
    if l[i]!=0:
        ans=ans*(l[i]+1)%(10**9+7)
print(ans%(10**9+7))