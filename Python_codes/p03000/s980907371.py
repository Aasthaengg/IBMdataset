n,x = map(int,input().split())
l = list(map(int,input().split()))
d = [0]
for i in range(1,n+1):
    d.append(d[i-1]+l[i-1])

ans = 0

for dd in d:
    if dd <= x:
        ans += 1
print(ans)