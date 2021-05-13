n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = []
for _ in range(n):
    d = list(map(int,input().split()))
    a.append(d)

ans = 0
for i in range(n):
    tmp = 0
    for j in range(m):
        tmp += b[j]*a[i][j]
    tmp += c
    if tmp > 0:
        ans += 1

print(ans)