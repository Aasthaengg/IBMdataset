N,x=map(int,input().split())
a=list(map(int,input().split()))
temp=x
ans=0
a.sort()
i=-1
while True:
    i+=1
    x-=a[i]
    if x<0:
        break
    ans+=1
    if ans==N:
        break
if sum(a)<temp:
    ans-=1
    
print(ans)
