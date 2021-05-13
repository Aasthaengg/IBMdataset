n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 10**10

for i in range(n-k+1):
    tmp = h[i] - h[i+k-1]
    ans = min(ans, tmp)

print(ans)