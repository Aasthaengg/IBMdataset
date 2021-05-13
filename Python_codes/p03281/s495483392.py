n = int(input())
f = [0 for i in range(n+1)]
for i in range(1,n+1):
    cur = i
    while cur<=n:
        f[cur] += 1
        cur += i 

ans = 0
for i in range(1,n+1):
    if i%2==1 and f[i]==8:
        ans += 1

print(ans)