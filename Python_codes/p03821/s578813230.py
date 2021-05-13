import math

N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


ans = 0

for a, b in zip(A[::-1], B[::-1]):
    a += ans
    ans += math.ceil(a / b) * b - a

print(ans)