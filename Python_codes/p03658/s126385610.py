from sys import stdin
import math

[N, K] = list(map(int, stdin.readline().rstrip().split()))
l = list(map(int, stdin.readline().rstrip().split()))
l_sorted = sorted(l, reverse=True)

total_length=0
for i in range(K):
    total_length += l_sorted[i]

print(total_length)
