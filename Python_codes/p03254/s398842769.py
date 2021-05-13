n,x=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*n
a.sort()
cnt=0
for i in range(n):
    if a[i]<=x:
        x-=a[i]
        if i==n-1 and x!=0:
            break
        cnt+=1
    else:
        break
print(cnt)
