
N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

MAX = N + 2
array = [0] * (MAX)

for l, r in X:
    array[l] += 1
    array[r + 1] -= 1

for i in range(MAX - 1):
    array[i + 1] += array[i]

print(sum(v == M for v in array))
