n,k = map(int,input().split())
x = [int(input()) for i in range(n)]
x.sort()
ans = float('inf')
for i in range(n-k+1):
    ans = min(ans,x[i+k-1]-x[i])
print(ans)