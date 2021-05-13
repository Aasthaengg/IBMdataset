N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
ans=0
position=1
flag=True
for i in range(N):
    if position==2:
        print(ans)
        flag=False
        break 
    else:
        position=a[position-1]
        ans+=1

if flag:
    print(-1)