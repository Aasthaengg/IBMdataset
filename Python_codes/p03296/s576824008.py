n=int(input())
a=list(map(int,input().split()))
l=[]
t=0

for i in range(n-1):
    if i==n-2:
        if a[i+1]==a[i]:
            t+=2
            l.append(t)
        else:
            t+=1
            l.append(t)
            l.append(1)
        continue      
    if a[i+1]==a[i]:
        t+=1
    else:
        t+=1
        l.append(t)
        t=0
# print(l)
ans=0
for ll in l:
    ans+=ll//2
print(ans)