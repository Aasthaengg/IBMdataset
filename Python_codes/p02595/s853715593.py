import math

n, d = list(map(int, input().split()))
d2 = d ** 2
cnt = 0

for _ in range(n):
    x, y = list(map(int, input().split()))
    if x ** 2 + y ** 2 <= d2:
        cnt += 1

print(cnt)