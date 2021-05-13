N,K = map(int, input().split())
h = list(map(int, input().split()))

DP=[0]*(N)
DP[0]=0
DP[1]=abs(h[1]-h[0])
#print(DP)
for i in range(2,N):
    DP[i]=DP[i-1]+abs(h[i]-h[i-1])
    for u in range(1,K+1):
        if i-u>=0:
            DP[i]=min(DP[i],DP[i-u]+abs(h[i]-h[i-u]))
        else:
            break
    #print(DP)
print(DP[N-1])