h,w=map(int,input().split())
n=int(input())
a=[0]+list(map(int,input().split()))
ans=[[0]*w for i in range(h)]
x=0
y=0
for i in range(1,n+1):
    for _ in range(a[i]):
        
        if y==w:
            x+=1
            y=0
            
        if x%2==0:
            ans[x][y]=i
            y+=1
        else:
            ans[x][w-1-y]=i
            y+=1
for u in ans:
    print(*u)