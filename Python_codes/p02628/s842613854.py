N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

ans = 0
for index in range(K):
    ans += p[index]

print(ans)