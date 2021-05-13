
N = int(input())

ctr = [1] * (N + 1)
for n in range(2, N + 1):
    for v in range(n, N + 1, n):
        ctr[v] += 1

ans = 0
for n in range(1, N + 1):
    ans += n * ctr[n]
print(ans)
