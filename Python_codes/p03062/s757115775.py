n=int(input())
a=list(map(int,input().split()))
cnt=0
ans=0
m=10**9+1
for i in a:
    if i<0: cnt+=1
    ans+=abs(i)
    if abs(i)<m: m=abs(i)
if cnt%2==0:
    print(ans)
else:
    print(ans-m*2)