import math

N, M = map(int, input().split())
counter = 0
for _ in range(N):
    a, b = map(int, input().split())
    distance = math.sqrt(abs(a)**2 + abs(b)**2)

    if distance <= M:
        counter += 1

print(counter)