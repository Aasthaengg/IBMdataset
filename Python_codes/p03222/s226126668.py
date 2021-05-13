from collections import defaultdict

H, W, K = list(map(int, input().split()))

mapping = defaultdict(int)

for source in range(1 << (W - 1)):
    l = [False for _ in range(W - 1)]
    for i in range(W - 1):
        l[i] = bool(source & (1 << i))
    flag = True
    for i in range(W - 2):
        if l[i] and l[i + 1]:
            # invalid
            flag = False
            # print("break",l)
            break
    if not flag:
       continue

    for i in range(W):
        if i > 0 and l[i - 1]:  # decrement
            mapping[i, i - 1] += 1
        elif i < W - 1 and l[i]:  # increment
            mapping[i, i + 1] += 1
        else:
            mapping[i, i] += 1

last = [1] + [0] * (W - 1)
for _ in range(H):
    current = [0] * W
    for (start, dst), count in mapping.items():
        current[dst] += last[start] * count
        current[dst] = current[dst] % (10**9+7)
    last = current
print(last[K - 1] %(10**9+7))