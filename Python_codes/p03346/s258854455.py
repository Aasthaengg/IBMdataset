from sys import stdin
N = int(stdin.readline().rstrip())
LIS = [0] * (N + 1)
P = [0]*N
for i in range(N):
    P[i] = int(stdin.readline().rstrip())
for p in P:
    LIS[p] = LIS[p-1] + 1 
print(N - max(LIS))