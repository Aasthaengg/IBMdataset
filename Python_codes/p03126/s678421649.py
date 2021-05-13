from collections import Counter
N, M = map(int, input().split())
c = Counter()
for i in range(N):
    K, *A = list(map(int, input().split()))
    c.update(A)
r = 0
for k, v in c.items():
    if v == N:
        r += 1
print(r)
