import bisect
N, M = map(int, input().split())
A = sorted(map(int, input().split()))
for _ in range(M):
    x = A.pop()
    y = x // 2
    i = bisect.bisect_left(A, y)
    A.insert(i, y)
ans = sum(A)
print(ans)