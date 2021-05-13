def inp():return map(int,input().split())

n,d=inp()
k=0
ans=0
while k<n:
    k=k+d*2+1
    ans+=1
print(ans)