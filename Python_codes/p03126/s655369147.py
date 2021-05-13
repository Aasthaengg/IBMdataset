n,m = map(int,input().split())
l = []
for _ in range(n):
    a = list(map(int,input().split()))
    l.append(a)

b = []

for i in range(n):
    for j in range(1,l[i][0]+1):
        b.append(l[i][j])

ans = 0
for k in range(1,m+1):
    cnt = b.count(k)
    if cnt == n:
        ans += 1

print(ans)