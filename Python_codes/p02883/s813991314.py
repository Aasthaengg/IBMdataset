from heapq import heappush, heappop

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

F.sort()
x = [a * b for a, b in zip(F, sorted(A, reverse=True))]

ub = max(x)
lb = 0
while ub - lb > 1:
    mid = (ub + lb) // 2
    res = 0
    for i in range(N):
        tmp = max(0, x[i] - mid)
        res += -(-tmp // F[i])

    if res <= K:
        ub = mid
    else:
        lb = mid

if sum(A) <= K:
    print(0)
else:
    print(ub)

