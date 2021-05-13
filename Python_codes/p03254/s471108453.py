N, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

a.sort()
ans = 0

for i in a:
    if x >= i:
        ans += 1
        x -= i
    else:
        x = 0
        break
        
if x > 0:
    ans -=1
print(ans)