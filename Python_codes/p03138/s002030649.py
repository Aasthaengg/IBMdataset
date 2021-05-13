
N, K = map(int, input().split())
X = list(map(int, input().split()))

# Calculate numbers of bits
bits = [0] * 40
for k in range(40):
    for v in X:
        bits[k] += v >> k & 1

# Take larger # of bits
ctr = [0] * 41
for k in range(40):
    ctr[k + 1] = ctr[k] + (max(N - bits[k], bits[k]) << k)

res = 0
cnt = 0
for i in reversed(range(40)):
    if K >> i & 1:
        res = max(res, cnt + (bits[i] << i) + ctr[i])
        cnt += (N - bits[i]) << i
    else:
        cnt += bits[i] << i

print(max(res, cnt))
