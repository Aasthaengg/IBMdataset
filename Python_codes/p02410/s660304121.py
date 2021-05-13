from operator import mul

n, m = map(int, input().split())
a = [map(int, input().split()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

for ai in a:
    print(sum(map(mul, ai, b)))