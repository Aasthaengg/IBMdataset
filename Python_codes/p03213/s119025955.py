from collections import Counter

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

def fac(n):
    ans=1
    for i in range(n,0,-1):
        ans*=i
    return ans

n=int(input())
c = Counter(prime_factorize(fac(n)))
v=c.values()
cnt={74:0,24:0,14:0,4:0,2:0}
for i in v:
    if i>=74:
        cnt[74]+=1
    if i>=24:
        cnt[24]+=1
    if i>=14:
        cnt[14]+=1
    if i>=4:
        cnt[4]+=1
    if i>=2:
        cnt[2]+=1
ans=cnt[74]+cnt[24]*(cnt[2]-1)+cnt[14]*(cnt[4]-1)+cnt[4]*(cnt[4]-1)*(cnt[2]-2)//2
print(ans)