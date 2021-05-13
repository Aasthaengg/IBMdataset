#%%
n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
tmp = 0
flag = True
if a[0] != 0:
    flag = False

for i in range(n-1):
    if a[i+1] > a[i]:
        pass
    else:
        ans += a[i]
    if a[i+1] - a[i] > 1:
        flag = False
    
ans += a[n-1]

if flag:
    print(ans)
else:
    print(-1)
