from itertools import accumulate
n, k = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(k):
    new_A = [0]*(n+1)
    cnt = 0
    for i in range(n):
        a = A[i]
        if a == n:
            cnt += 1
        L = max(0, i-a)
        R = min(n, i+a+1)
        new_A[L] += 1
        new_A[R] -= 1
    A = list(accumulate(new_A))
    if cnt == n:
        break

print(*A[:-1])
