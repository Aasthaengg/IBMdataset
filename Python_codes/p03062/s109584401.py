n=int(input())
a=list(map(int,input().split()))
cnt=0
ans=0
mini=10000000000
for i in a:
    if i<0:
        cnt+=1
    p=abs(i)
    ans+=p
    if p<mini:
        mini=p
if cnt%2==1:
    ans-=mini*2
print(ans)