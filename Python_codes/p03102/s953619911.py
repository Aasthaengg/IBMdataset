 
n,m,c = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    d = 0
    for j in range(m):
        d = d + a[j]*b[j]
    if d+c > 0:
        ans = ans + 1
print(ans)