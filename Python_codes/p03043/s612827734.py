import math

n, k = map(int, input().split())

# for small
score = 0
times = []
for i in range(1, min(n + 1, k)):
    times.append(math.ceil(math.log2((k / i))))

if len(times):
    bottom_max = times[0]
    for t in times:
        score += 2 ** (bottom_max - t)
    score /= 2 ** (bottom_max) * n

# for big
big = [i for i in range(k, max(k, n + 1))]
score += len(big) / n
print('{:.10f}'.format(score))
