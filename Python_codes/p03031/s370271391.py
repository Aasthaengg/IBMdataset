N, M = map(int, input().split())
A = []
for _ in range(M):
    A.append(tuple(map(int, input().split())))
P = tuple(map(int, input().split()))
import itertools
def hantei(A, RETU, P):
    for i in range(len(A)):
        count = 0
        for k in RETU:
            if k in A[i][1:]:
                count += 1
        if not count % 2 == P[i]:
            return False
    return True
ans = 0
for i in range(1, N + 1):
    for k in itertools.combinations(range(1, N + 1), i):
        if hantei(A, k, P):
            ans += 1
if hantei(A, [0], P):
    ans += 1
print(ans)