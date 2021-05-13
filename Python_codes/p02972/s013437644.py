from math import sqrt, ceil

n = int(input())
data = list(map(int, input().split()))
balls = []

mid = n//2+1
table = [0] * n
for idx in range(mid-1, n):
    table[idx] = data[idx]
    if data[idx] == 1:
        balls.append(idx+1)
for idx in range(mid-2, -1, -1):
    score = 0
    for idx2 in range(idx, n, idx+1):
        score += table[idx2]
    if score%2 != data[idx]:
        table[idx] = 1
        balls.append(idx+1)

print(len(balls))
if len(balls) > 0:
    print(' '.join(map(str, balls)))