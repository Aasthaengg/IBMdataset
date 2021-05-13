n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n):
    if p[i]-1==i:
        if i<n-1:p[i],p[i+1] = p[i+1],p[i]
        ans += 1
print(ans)