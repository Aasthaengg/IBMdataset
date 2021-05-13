n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
i = 0
while x >= a[i]:
    if i == n-1:
        if a[i] == x:
            ans+=1
            break
        else:
            break
    x -= a[i]        
    i += 1
    ans += 1
print(ans)