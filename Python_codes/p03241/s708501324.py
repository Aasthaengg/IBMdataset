N, M = map(int, input().split())

ans = 1
for i in range(1, int(M**0.5)+1):
    if M % i != 0:
        continue

    j = M // i
    if i * N <= M:
        ans = max(ans, i)
    if j * N <= M:
        ans = max(ans, j)

print(ans)
