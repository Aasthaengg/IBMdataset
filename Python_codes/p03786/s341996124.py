from itertools import accumulate

N = int(input())
A = list([int(x) for x in input().split()])

A.sort()

check = list(accumulate(A))

for key in range(N-1, 0, -1):
    if check[key-1] * 2 < check[key] - check[key-1]:
        print(N - key)
        exit()

print(N)
