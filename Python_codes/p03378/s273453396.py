n,m,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for i in range(m):
    if a[i]<x:
        ans += 1
    else:
        break

print(min(ans,m-ans))