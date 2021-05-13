N = int(input())
K = int(input())
ans = 1 << 50
for i in range(1 << N):
    x = 1
    for j in range(N):
        if i >> j & 1:
            x *= 2
        else:
            x += K
    ans = min(ans, x)
print(ans)
