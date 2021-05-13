import sys
import copy

sys.setrecursionlimit(10**6)

m = [0,2,5,5,4,5,6,3,7,6]

def a_le_b(a, b):
    la, lb = len(a), len(b)
    if la == lb:
        for i in range(la):
            if a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
        return True
    return la < lb

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(len(A)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if m[A[i]] == m[A[j]]:
            del A[i]
            break
# print(A)
dp = [[] for _ in range(N+1)]

for i in range(N):
    if len(dp[i])==0 and i != 0: continue
    x = copy.copy(dp[i]) + [0]
    # print(x)
    for j in range(len(A)):
        ind = i + m[A[j]]
        if ind <= N:
            x[-1] = A[j]
            if a_le_b(dp[ind], x):
                dp[ind] = copy.copy(x)
# print(dp)
print(''.join(map(str, dp[-1])))
