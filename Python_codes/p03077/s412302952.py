N = int(input())
A = [int(input())for _ in range(5)]

now = 0
for i, a in enumerate(A):
    now = max((N - 1) // a + 1 + i, now + 1)
print(now)