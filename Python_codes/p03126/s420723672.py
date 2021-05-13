N, M = map(int, input().split())
A = []
for _ in range(N):
    s = list(map(int, input().split()))
    k = s[0]
    A.append(s[1:])

foods = [0] * M
for row in A:
    for a in row:
        foods[a-1] += 1
count = 0
for f in foods:
    if f == N:
        count += 1
print(count)

