import math

N = int(input())
D, X = map(int, input().split())

ans = 0
for i in range(N):
    A = int(input())
    ans += math.ceil(D / A)

print(ans + X)
