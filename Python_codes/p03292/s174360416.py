# A - Task Scheduling Problem

A = list(int(a) for a in input().split())
A.sort()

ans = 0
for i in range(1, 3):
    ans += abs(A[i] - A[i-1])

print(ans)