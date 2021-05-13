n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    A[i] -= (i+1)

A.sort()

med = [A[n//2]]
if n % 2 == 0:
    med.append(A[n//2 - 1])

ans = 1000000000000000000
for m in med:
    cnt = 0
    for a in A:
        cnt += abs(a-m)
    ans = min(ans, cnt)

print(ans)