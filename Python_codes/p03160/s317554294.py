n=list(map(int,input().split()))[0]
h=list(map(int,input().split()))

stair=[float('inf')]*(n)
stair[0]=0
for i in range(n-1):
    stair[i+1]=min(stair[i+1],stair[i]+abs(h[i]-h[i+1]))
    if i<n-2:
        stair[i+2]=min(stair[i+2],stair[i]+abs(h[i]-h[i+2]))

print(stair[-1])