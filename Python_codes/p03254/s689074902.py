n,x=map(int,input().split())
a=sorted([int(i)for i in input().split()])
res=0
if sum(a)==x:
    res=n
else:
    for i in range(n):
        if sum(a[:i])<=x:res=i
print(res)