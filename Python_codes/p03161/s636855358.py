n,k=map(int,input().split())
h=[int(i) for i in input().split()]
k=min(k,n-1)
dp=[0]

for i in range(1,k):
    x=[]
    for j in range(1,i+1):
        x.append(dp[i-j]+abs(h[i-j]-h[i]))
    dp.append(min(x))

for i in range(1,n-k+1):
    m=k+i-1
    x=[]
    for j in range(1,k+1):
        x.append(dp[m-j]+abs(h[m-j]-h[m]))
    dp.append(min(x))

print(dp[-1])
