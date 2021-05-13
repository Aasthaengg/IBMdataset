n = int(input().rstrip())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))
ans = 0
for i in range(n):
    ans += min(a[i],b[i]) + min(a[i+1],max(0,b[i]-a[i]))
    a[i+1] -= min(a[i+1],max(0,b[i]-a[i]))
print(ans)