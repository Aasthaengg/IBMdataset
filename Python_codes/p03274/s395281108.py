n,k = map(int, input().split())
x = list(map(int, input().split()))
ans = float("inf")
for i in range(0,n-k+1):
    if (x[i]<=0 and x[i+k-1]<=0):
        ans = min(ans, -x[i])
    elif (x[i]>=0 and x[i+k-1]>=0):
        ans = min(ans, x[i+k-1])
    else:
        ans = min (ans, x[i+k-1]-x[i]+(min(abs(x[i+k-1]),abs(x[i]))))
print(ans)