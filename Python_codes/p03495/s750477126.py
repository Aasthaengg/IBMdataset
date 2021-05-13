from collections import Counter

N, K = map(int, input().split(' '))
balls = tuple(map(int, input().split(' ')))

counter = Counter(balls)
counts = sorted(counter.values(), reverse=True)

print(sum(counts[K:]))
