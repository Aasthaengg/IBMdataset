n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dif=[]

s=0
ans=0
for g in range(n):
    if a[g]<b[g]:
        s+=b[g]-a[g]
        ans+=1
    elif a[g]>b[g]:
        dif.append(a[g]-b[g])
dif.sort(reverse=True)

if s==0:
    print(0)
    exit()

for l in range(len(dif)):
    s-=dif[l]
    ans+=1
    if s<0:
        break

if s<=0:
    print(ans)
else:
    print(-1)