n=int(input())
a=sorted([int(i)for i in input().split()])
res=0
for i in range(n):
    tmp=a.pop(-1)
    if i%2==0:
        res+=tmp
    else:
        res-=tmp
print(res)