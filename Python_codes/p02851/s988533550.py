n, k = map(int, input().split())
m = list(map(int, input().split()))
T = [0] * (n + 1)

b = 0
for i, a in enumerate(m):
    b += a - 1
    b %= k
    T[i + 1] = b

tmp = {}
count = 0

for i, b in enumerate(T):
    if i >= k:
        tmp[T[i - k]] -= 1

    if b in tmp:
        count += tmp[b]
        tmp[b] += 1
    else:
        tmp[b] = 1

print(count)