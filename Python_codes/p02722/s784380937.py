n = int(input())


def factor(n):
    res=set()
    for i in range(2,int(n**(1/2))+10):
        if n%i == 0:
            res.add(i)
            res.add(n//i)

    res.add(n)
    res.discard(1)
    return list(res)

ans = 0

ans += len(factor(n-1))


for k in factor(n):
    n2=n
    if k==1:
        continue
    while n2%k==0:
        n2//=k
    if n2%k == 1:
        ans +=1
        

print(ans)
