n,m,x = map(int,input().split())
a = [0]*n
for i in range(n):
    a[i] = list(map(int,input().split()))
ans = float("Inf")
for i in range(2**n):
    c = 0
    L = [0]*m
    for j in range(n):
        if (i>>j)&1:
            c += a[j][0]
            for k in range(m):
                L[k] += a[j][k+1]
    
    sw = 1
    for k in range(m):
        if L[k] < x:
            sw = 0
            break
    if sw == 1:
        ans = min(ans, c)
        
if ans == float("Inf"):
    print(-1)
else:
    print(ans)