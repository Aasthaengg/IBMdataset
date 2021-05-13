from collections import deque
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)
p = sum(1 for a in A if a > 0)
if A[-1] > 0:
    print(sum(A[:-1]) - A[-1])
    k = A[-1]
    for a in A[:-2]:
        print(k, a)
        k -= a
    print(A[-2], k)

elif A[0] < 0:
    print(A[0] - sum(A[1:]))
    k = A[0]
    for a in A[1:]:
        print(k, a)
        k -= a
else:
    print(sum(abs(a) for a in A))
    A = deque(A)
    k = A.pop()
    for _ in range(p-1):
        t = A.popleft()
        print(k, t)
        k -= t
    t = A.popleft()
    print(t, k)
    t -= k
    for a in A:
        print(t, a)
        t -= a
