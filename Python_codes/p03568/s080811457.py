from itertools import product

N = int(input())
A = list(map(int, input().split()))

s = sum(any(map(lambda x: x % 2 == 0, (u + v for u, v in zip(A, list(x)))))
        for x in product((-1, 0, 1), repeat=N))
print(s)
