n = int(input())
a = list(map(int,input().split()))
b = [0 for i in range(n+1)]
leaf = sum(a)

if n == 0 and a[0] != 1:
    print(-1)
    exit()
b[0] = 1 - a[0]
leaf -= a[0]
ans = 1
for i in range(1,n+1):
    kosu = min(b[i-1] * 2,leaf)
    ans += kosu
    b[i] = kosu - a[i]
    if b[i] < 0:
        print(-1)
        exit()
    leaf -= a[i]
print(ans)
