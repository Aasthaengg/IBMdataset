n=int(input())
a=[0]
for i in range(n):
    a.append(int(input()))
m=1
ans=0
for i in range(n):
    if m==2:
        print(ans)
        exit()
    else:
        m=a[m]
        ans+=1
print(-1)
            
