#090_D
n, k = map(int, input().split())
ans = 0
for b in range(k+1, n+1):
    ans += n // b * (b - k) + max(0, (n % b) - (k - 1))
print(ans if k > 0 else n ** 2)