n = int(input())

c = [[0]*10 for _ in range(10)]
for i in range(1,n+1):
    s = str(i)
    a = int(s[0])
    b = int(s[-1])
    c[a][b] += 1

ans = 0
for j in range(1,10):
    for k in range(1,10):
        ans += (c[j][k] * c[k][j])


print(ans)