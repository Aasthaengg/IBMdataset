import math

def can(X):
    training = 0
    for i in range(N):
        training += max(math.ceil(A[i] - X / F[i]), 0)
    return training <= K

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort(reverse=True)
F.sort()

a = 0
b = max(A) * max(F) * N
c = 0

while (b - a) >= 1:
    c = (a + b) / 2
    if can(c):
        b = c
    else:
        a = c

res = math.floor(c)

if can(res):
    print(res)
else:
    print(res + 1)