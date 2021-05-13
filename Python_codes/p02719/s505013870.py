n,k = map(int, input().split())
n = (n - (n//k-1)*k) if n > k else n
n_min = 0
while n_min <= n:
    n_min = abs(n-k)
    if n_min >= n and n < k:
        print(min(n_min, n))
        break
    n = n_min