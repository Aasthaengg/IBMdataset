n,c,k = map(int,input().split())
t = list(int(input()) for i in range(n))
t.sort()
ans = 0
x = t[0]
y = 1
for i in range(1,n):
    if x+k < t[i] or y >= c:
        ans += 1
        x = t[i]
        y = 1
    else:
        y += 1
print(ans+1)