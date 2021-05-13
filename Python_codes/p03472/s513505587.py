n,h=map(int,input().split())
th=[]
ma=0
for i in range(n):
    a,b=map(int,input().split())
    ma=max(ma,a)
    th.append([b,a])
ans=0
th.sort(reverse=True)
for i in range (n):
    if h>0 and th[i][0]>ma:
        h-=th[i][0]
        ans+=1
    if h<=0:
        print(ans)
        exit()
if h%ma==0:
    ans+=h//ma
else:
    ans+=1+(h//ma)
print(ans)

