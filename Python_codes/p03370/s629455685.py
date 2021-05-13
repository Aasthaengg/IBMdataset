n, x = [int(i) for i in input().strip().split()]

D = [int(input()) for _ in range(n)]

_min = min(D)

_sum = sum(D)

print(n + (x - _sum) // _min)
