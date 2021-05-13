from collections import Counter
n = int(input())
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

lst=[]
for i in range(n):
    lst.extend(prime_factorize(i+1))
lst=Counter(lst)
ans=1
INF=1000000007
for i in lst.values():
    ans*=i+1
    ans%=INF
print(ans)