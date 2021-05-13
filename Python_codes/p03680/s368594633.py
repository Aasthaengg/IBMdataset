n=int(input())
b=[0 for i in range(n+1)]
for i in range(n):
    b[i+1]=int(input())
now=1
ans=0
while ans<n+1:
    next=b[now]
    ans+=1
    now=next
    if next==2:
        print(ans)
        exit()
print(-1)