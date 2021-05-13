from itertools import accumulate
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = [0] * N
v = [0] * N
for i in range(N):
    x[i], v[i] = map(int, input().split())
clockwise = list(accumulate(v))
counterclockwise = list(accumulate(v[::-1]))[::-1]
for i in range(N):
    clockwise[i] -= x[i]
    counterclockwise[i] -= C-x[i]
clockwise_max = [0] * N
for i in range(1, N):
    clockwise_max[i] = max(clockwise_max[i-1], clockwise[i-1])
counterclockwise_max = [0] * N
for i in range(N-1)[::-1]:
    counterclockwise_max[i] = max(counterclockwise_max[i+1], counterclockwise[i+1])
ans = 0
for i in range(N):
    ans = max(ans, clockwise[i])
    ans = max(ans, clockwise[i]-x[i]+counterclockwise_max[i])
for i in range(N)[::-1]:
    ans = max(ans, counterclockwise[i])
    ans = max(ans, counterclockwise[i]-(C-x[i])+clockwise_max[i])
print(ans)
