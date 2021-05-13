from heapq import heappop, heappush
def inpl(): return list(map(int, input().split()))
N, M = inpl()
A = [0]*M
B = [0]*M
C = [0]*M
for m in range(M):
    A[m], B[m] = inpl()
    c = 0
    for x in inpl():
        c += pow(2, x-1)
    C[m] = c
DP = [10**9]*pow(2, N)
DP[0] = 0
for i in range(pow(2, N)):
    if DP[i] > 10**8:
        continue
    for m in range(M):
        DP[i|C[m]] = min(DP[i|C[m]], DP[i] + A[m])
print(DP[-1] if DP[-1] < 10**9 else -1)