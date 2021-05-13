N,K = map(int,input().split())
h = list(map(int,input().split()))
#print(h)
DP = [10**9]*N
DP[0] = 0
DP[1] = abs(h[1]-h[0])
for i in range(2,N):
    for j in range(max(i-K,0),i):
        DP[i] = min(DP[i], DP[j] + abs(h[i]-h[j]))
    #print(DP[i])
print(DP[-1])