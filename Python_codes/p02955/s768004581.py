import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
d=set()
for i in range(1,int(sum(a)**0.5)+5):
    if s%i==0: d.add(i);d.add(s//i)
d=sorted(list(d),reverse=True)
for x in d:
    b=sorted([a[i]%x for i in range(n)],reverse=True)
    s=sum(b)
    p=s//x
    if s-sum(b[:p])<=k: break
print(x)