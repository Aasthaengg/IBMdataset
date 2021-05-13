n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
mod = 10**9 + 7

ans = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j] and i>j:
            ans += (k-1) * k//2
        if a[i] >a[j] and i<j:
            ans += k * (k+1) // 2
    ans = ans % mod
print(ans)