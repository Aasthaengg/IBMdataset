import math

n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.reverse()
B.reverse()

cnt = 0
for a, b in zip(A, B):
    a += cnt
    cnt += math.ceil(a/b) * b - a
print(cnt)