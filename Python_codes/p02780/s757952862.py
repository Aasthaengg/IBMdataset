n,k = map(int,input().split())
p = list(map(int,input().split()))
ans = sum(p[0:k])
t = ans
for i in range(1,n-k+1):
    t += - p[i-1] + p[i+k-1]
    ans = max(ans,t)
print((ans + k) / 2)