n,k = map(int,input().split())
a = list(map(int,input().split()))
x = 0
y = 0
mod = 10**9 + 7
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            if i > j:
                x += 1
            if i < j:
                x += 1
                y += 1
ans = x*k*(k-1)//2 % mod
ans += y*k % mod
ans %= mod
print(ans)