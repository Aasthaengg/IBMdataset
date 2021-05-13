n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            count += (k*(1+k) // 2) % mod
        if a[i] < a[j]:
            count += ((k-1)*k // 2) % mod
print(count % mod)