n=int(input())
a=list(map(int,input().split()))
m=sum(a)/n
l=[0]*n
for i in range(n):
    l[i]=abs(m-a[i])
x=min(l)
for i in range(n):
    if l[i]==x:
        print(i)
        break

