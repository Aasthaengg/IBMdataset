n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=[0,0,0,0,0,0,0,0,0]
for i in range(n):
    if a[i]<400:
        ans[0]=1
    if 400<=a[i]<800:
        ans[1]=1
    if 800<=a[i]<1200:
        ans[2]=1
    if 1200<=a[i]<1600:
        ans[3]=1
    if 1600<=a[i]<2000:
        ans[4]=1
    if 2000<=a[i]<2400:
        ans[5]=1
    if 2400<=a[i]<2800:
        ans[6]=1
    if 2800<=a[i]<3200:
        ans[7]=1
    if 3200<=a[i]:
        ans[8]+=1
cnt=0
for i in range(8):
    if ans[i]!=0:
        cnt+=1
cnt2=cnt
if ans[8]!=0:
    cnt2=cnt+ans[8]
print(max(1,cnt),cnt2)
