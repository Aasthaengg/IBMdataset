N, K = map(int, input().split())

ans = 0

num = [0] * (K+1)
for i in range(1, N+1):
    num[i % K] += 1

for a in range(K+1):
    b = (K-a) % K
    c = (K-a) % K
    if ((b+c) % K) == 0:
        ans += (num[a] * num[b] * num[c])

print(ans)
