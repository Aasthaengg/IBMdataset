n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()

for i in range(n-k+1):
    a = h[i+k-1]-h[i]
    ans = a if i == 0 else min(ans, a)

print(ans)
