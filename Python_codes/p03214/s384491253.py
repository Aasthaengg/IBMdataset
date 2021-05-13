n=int(input())
o=list(map(int,input().split()))
a=sum(o)/n
dif=1000000000
ans=-1
for i,k in enumerate(o):
    if abs(a-k)<dif:
        dif=abs(a-k)
        ans=i
print(ans)