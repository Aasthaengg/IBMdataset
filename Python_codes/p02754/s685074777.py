def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n,a,b=sep()
k=n//(a+b)
ans=(k*a)
k2=n%(a+b)
if k2<=a:
    ans+=k2
else:
    ans+=a
print(ans)