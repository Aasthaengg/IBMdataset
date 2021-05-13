n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n-1) :
    if a[i+1] - a[i] >= 0 :
        continue
    else :
        ans += abs(a[i+1] - a[i])
        a[i+1] += abs(a[i+1] - a[i])
print(ans)