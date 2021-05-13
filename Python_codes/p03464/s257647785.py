from math import ceil
K = int(input())
A = list(map(int, input().split()))
L, R = 2, 2

for n in A[::-1]:
    L = ceil(L / n) * n
    R = (R // n) * n + n - 1
    if L > R:
        print(-1)
        exit()

print(L, R)
