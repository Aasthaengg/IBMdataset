N = int(input())
X = [map(int, input().split()) for _ in range(N)]
ans = 0

for i in range(N):
    l, r = X[i]
    ans += r - l + 1

print(ans)