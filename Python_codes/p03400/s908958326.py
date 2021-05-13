import math

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

count = 0
for a in A:
    count += math.ceil(D / a)

print(count + X)