n,k = map(int,input().split())
x = list(map(int,input().split()))
ans = float('inf')
for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    w1 = abs(l)+abs(r-l)
    w2 = abs(r)+abs(l-r)
    ans = min(ans, min(w1,w2))
print(ans)