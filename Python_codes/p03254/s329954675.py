n,x = map(int,input().split())
a = sorted(map(int,input().split()))
ans = 0

for i in a[:-1]:
    if i <= x:
        ans += 1
        x -= i
    else:
        break
        
if x == a[-1]:
    ans += 1
    
print(ans)