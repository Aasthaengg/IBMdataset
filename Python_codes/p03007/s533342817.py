from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = sum(abs(a) for a in A)
if A[0] >= 0:
    ans -= 2 * A[0]
elif A[-1] < 0:
    ans += 2 * A[-1]
print(ans)
nonneg_idx = bisect_left(A, 0)
if nonneg_idx == 0:
    nonneg_idx = 1
elif nonneg_idx == N:
    nonneg_idx = N - 1
acc = A[nonneg_idx - 1]
for a in A[nonneg_idx + 1 :]:
    print(acc, a)
    acc -= a
print(A[nonneg_idx], acc)
acc = A[nonneg_idx] - acc
for a in A[: nonneg_idx - 1]:
    print(acc, a)
    acc -= a
