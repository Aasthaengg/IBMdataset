N = int(input())
h = list(map(int, input().split()))

ans = 0
p = 0
for i in range(N):
    if p <= h[i]:
        ans += h[i]-p
    p = h[i]
print(ans)