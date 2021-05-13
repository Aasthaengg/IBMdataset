N,K = map(int,input().split())
h=[]
for _ in range(N):
    h.append(int(input()))
h.sort()
ans = float('inf')
for i in range(N-K+1):
    ans=min(ans,h[i+K-1]-h[i])
print(ans)