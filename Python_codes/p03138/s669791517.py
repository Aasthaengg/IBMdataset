N, K = map(int, input().split())
A = list(map(int, input().split()))

b = [0] * 40
for i in range(40):
    for k in A:
        b[i] += (k & (1 << i)) >> i

c = [0] * 40
for i in range(39):
    if b[i] > N - b[i]:
        c[i + 1] = c[i] + (b[i] << i)
    else:
        c[i + 1] = c[i] + (N - b[i] << i)

ans = 0
cnt = 0
for i in reversed(range(40)):
    if K & (1 << i):
        ans = max(ans, cnt + (b[i] << i) + c[i])
        cnt += N - b[i] << i
    else:
        cnt += b[i] << i
print(max(ans, cnt))
