from statistics import median
N = int(input())
A, B = zip(*tuple(tuple(map(int, input().split())) for _ in range(N)))
print(int((median(B) - median(A)) * (1 + (not N & 1))) + 1)