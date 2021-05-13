n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

l=make_divisors(s)
ans=1
for y in l[1:]:
    x=[i%y for i in a]
    x.sort()
    ss=sum(x)
    l1=[0]
    for i in range(n):
        l1.append(l1[-1]+x[i])
    l2=[0]
    for i in range(n):
        l2.append(l2[-1]+y-x[-i-1])
    l2.reverse()
    c=-1
    for i in range(n+1):
        if l1[i]==l2[i]:
            c=l1[i]
            break
    if c>-1 and c<=k:
        ans=max(ans,y)

print(ans)
