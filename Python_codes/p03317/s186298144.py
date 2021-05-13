n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1 if n//k > 0 else 0 
mod = (n-k)//(k-1) + min((n-k)%(k-1), 1)
print(ans + mod)