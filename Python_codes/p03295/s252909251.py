from operator import itemgetter

N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]
AB.sort(key = itemgetter(1))

counter = 0
last_b = -1
for a, b in AB:
    if a >= last_b:
        counter += 1
        last_b = b

print(counter)
