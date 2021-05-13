n = int(input())
h = list(map(int,input().split()))
A = []
ans = 0
res = 0
for i in range(n-1):
    if h[i]>=h[i+1]:
        ans += 1

    else:
        res = max(res,ans)
        ans = 0


res = max(res,ans)        
print(res)
