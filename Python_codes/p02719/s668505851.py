n, k = map(int, input().split())
mod = abs(n-k) % k
print(min(mod, k-mod))