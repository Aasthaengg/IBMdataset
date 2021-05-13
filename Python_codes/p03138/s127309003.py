n,k = map(int,input().split())
a = list(map(int,input().split()))

x = 0
ans = 0
for i in range(45,-1,-1):
    count = 0
    for j in a:
        if (j >> i) & 1:
            count += 1
    
    if n-count > count and x + (1<<i) <= k:
        ans += (n-count)* (1<<i)
        x += 1<<i
    else:
        ans += count*(1<<i)
print(ans)
