n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    ans += (n+1)//i * max(0, i-k)
    ans += max(0, (n+1) % i - k)
print(ans-n if k == 0 else ans)
