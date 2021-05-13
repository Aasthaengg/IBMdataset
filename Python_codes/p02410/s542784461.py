from operator import mul

n, m = map(int, input().split(' '))

A = []
B = []

for i in range(n):
    A.append(list(map(int, input().split(' '))))

for j in range(m):
    B.append(int(input()))

for a in A:
    print(sum(map(mul, a, B)))