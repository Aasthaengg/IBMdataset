from math import factorial
n=int(input())
cnt=[0]*(n+1)
lst=list(map(int,input().split()))
tmp=[0]*(n+1)
change=[0]*(n+1)
for i in lst:
    cnt[i]+=1
ans=0
for i in range(n+1):
    p=cnt[i]
    if p>=2:
        q=factorial(p)//factorial(p-2)//2
        ans+=q
        tmp[i]=q
    if p>=3:
        change[i]=factorial(p-1)//factorial(p-3)//2
for i in range(n):
    print(ans-tmp[lst[i]]+change[lst[i]])