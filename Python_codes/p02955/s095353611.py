n,k=map(int,input().split())
l=list(map(int,input().split()))
x=sum(l)
def f(m,k,l):
    l=[i%m for i in l]
    l.sort()
    if sum(l[:n-sum(l)//m])<=k:
        return True
ans=1
for i in range(1,int(x**0.5)+1):
    if x%i:
        continue
    if f(x//i,k,l):
        print(x//i)
        break
    elif f(i,k,l):
        ans=i
else:
    print(ans)