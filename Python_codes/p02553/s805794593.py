a = list(map(int,input().split()))
ans = -float('inf')
for i in range(2):
    for j in range(2,4):
        ans = max(ans,a[i]*a[j])
print(ans)