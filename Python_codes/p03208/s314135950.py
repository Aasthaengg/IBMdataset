n,k = map(int,input().split())
h = sorted([int(input()) for _ in range(n)])
ans = h[k-1]-h[0]
for i in range(n-k+1):
    m = h[i+k-1]-h[i]
    ans = min(m,ans)
print(ans)