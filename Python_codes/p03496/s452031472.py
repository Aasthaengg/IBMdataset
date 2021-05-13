N = int(input())
A = [int(_) for _ in input().split()]
B = [abs(a) for a in A]
absmaxv = -1
absmaxi = -1
for i, v in enumerate(B):
    if v > absmaxv:
        absmaxi, absmaxv = i, v
print(2 * N)
if A[absmaxi] > 0:
    print(absmaxi + 1, 1)
    print(absmaxi + 1, 1)
    for i in range(1, N):
        print(i, i + 1)
        print(i, i + 1)
else:
    print(absmaxi + 1, N)
    print(absmaxi + 1, N)
    for i in range(N, 1, -1):
        print(i, i - 1)
        print(i, i - 1)
