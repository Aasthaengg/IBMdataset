n=int(input())
l=[0]*n
for i in range(n):
    l[int(input())-1]=i
pre=-1
now=0
ans=n
for i in l:
    if pre<i:
        now+=1
    else:
        ans=min(ans,n-now)
        now=1
    pre=i

print(min(ans,n-now))