import math

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# M, D = map(int, input().split())
# A = list(map(int, input().split()))
# S = input()
memo = 10 ** 100
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0 and memo > (N // i) + i:
        memo = i + (N // i)

print(memo - 2)
