N,K = map(int,input().split())
h = []
for i in range(0,N):
    h.append(int(input()))
h.sort()
ans = 10**100
for i in range(0,N-K+1):
    ans = min(ans,h[i+K-1]-h[i])
print(ans)    
