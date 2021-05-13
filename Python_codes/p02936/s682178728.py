import sys
sys.setrecursionlimit(2*10**9)
N, Q = map(int, input().split())
A = [[] for _ in range(N)]
for _ in range(N-1):
    i, k = map(int, input().split())
    A[i-1].append(k-1)
    A[k-1].append(i-1)
n_P = [0] * N
for _ in range(Q):
    k, n = map(int, input().split())
    n_P[k-1] += n
ans = [0] * N
visited = [0] * N
def make(num, p):
    ans[num] += n_P[num] 
    ans[num] += p
    visited[num] = 1
    for i in A[num]:
        if visited[i] == 0:
            make(i,ans[num])
    return
make(0, ans[0])
print(*ans)