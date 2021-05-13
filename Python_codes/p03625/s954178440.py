n=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
cnt=1
li=[]
x=[0]
for i in range(n-1):
    if a[i+1]==a[i]:
        cnt+=1
    else:
        cnt=1
    if cnt==2:
        li.append(a[i+1])
    if cnt==4:
        x.append(a[i+1])

if len(li)>=2:
    print(max(li[0]*li[1],max(x)**2))
else:
    print(0)