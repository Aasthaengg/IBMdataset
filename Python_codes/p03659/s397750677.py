n = int(input())
a = list(map(int, input().split()))

S = sum(a)
snuke = 0
ans = float('inf')

for i in range(n-1):
    snuke += a[i]
    S -= a[i]
    ans = min(ans, abs(S-snuke))

print(ans)