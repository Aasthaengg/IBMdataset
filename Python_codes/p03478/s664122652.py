n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    s = 0
    for t in str(i):
        s += int(t)
    if a-1< s < b+1:
        ans += i
print(ans)