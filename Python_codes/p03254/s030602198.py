n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cnt=0
if sum(a)==x:
    print(n)
    exit()
else:
    for i in range(n-1):
        if a[i]<=x:
            x-=a[i]
            cnt+=1
print(cnt)