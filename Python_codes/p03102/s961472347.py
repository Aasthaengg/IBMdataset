n,m,c = map(int,input().split())
b = [int(s) for s in input().split()]
ans = 0
for i in range(n):
    check = c
    a = [int(s) for s in input().split()]
    for j in range(m):
        check = check + a[j] * b[j]
    if check > 0:
        ans += 1
print(ans)