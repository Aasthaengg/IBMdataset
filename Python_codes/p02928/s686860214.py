n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(a)
ans = 0
for i in range(n):
    x = 0
    y = 0
    for j in range(i):
        if a[i] > a[j]:
            x += 1
    for j in range(n):
        if a[i] > b[j]:
            y += 1
    ans += y*((1+k)*k//2) - x*k
    ans %= (10 ** 9 + 7)
print(ans)