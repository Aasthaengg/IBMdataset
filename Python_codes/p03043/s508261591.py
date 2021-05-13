n, k = [int(v) for v in input().split()]
rate = []
for i in range(1, n + 1):
    if i >= k:
        rate.append(1)
        continue

    for s in range(1, k):
        score = i * (2 ** s)
        if score >= k:
            rate.append(1 / (2 ** s))
            break

print(sum(rate) / len(rate))
