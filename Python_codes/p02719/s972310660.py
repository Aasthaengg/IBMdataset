(n, k) = tuple(map(int, input().split()))

mod = n % k
ans = min(mod, k - mod)
print(ans)
