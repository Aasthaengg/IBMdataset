n = int(input())
p = 0
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
        p += 1
    else:
        ans = max(p,ans)
        p = 0
if max(p,ans) >= 3:
    print('Yes')
else:
    print('No')