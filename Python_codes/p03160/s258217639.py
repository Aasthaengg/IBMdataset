N = int(input())
h = list(map(int,input().split()))

DP = [10**10]*N

DP[0] = 0
DP[1] = min(DP[1],DP[0]+abs(h[1]-h[0]))

for i in range(2,N):
    DP[i] = min(DP[i],DP[i-2]+abs(h[i]-h[i-2]))
    DP[i] = min(DP[i],DP[i-1]+abs(h[i]-h[i-1]))
    
print(DP[-1])