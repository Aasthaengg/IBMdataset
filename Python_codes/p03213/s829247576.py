import itertools

n=int(input())

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

a=[]
for i in range(2,n+1):
    aa=prime_decomposition(i)
    a.extend(aa)
    
a.sort()

i75=0
i25=0
i15=0
i5=0
i3=0
gr = itertools.groupby(a)
for key, group in gr:
    ll=len(list(group))
#    print(ll)
    if ll>=74:
        i75+=1
    if ll>=24:
        i25+=1
    if ll>=14:
        i15+=1
    if ll>=4:
        i5+=1
    if ll>=2:
        i3+=1
ans=0
ans=ans+i75
ans=ans+i25*max(i3-1,0)
ans=ans+i15*max(i5-1,0)
ans=ans+i5*max(i5-1,0)*max(i3-2,0)//2
print(ans)
