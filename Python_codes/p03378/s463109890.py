n,m,x = map(int,input().split())
a = list(map(int,input().split()))
i = x
ans = 0
while i > 0:
    i -= 1
    if i in a:
        ans += 1
c = 0
i = x
while i < n:
    i += 1
    if i in a:
        c += 1
ans = min(ans,c)
print(ans)