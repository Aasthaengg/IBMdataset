n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(1,n-1):
    t = p[i-1:i+2]
    if max(t)>t[1]>min(t):
        ans+=1
print(ans)