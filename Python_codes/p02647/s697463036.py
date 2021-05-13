n,k = map(int,input().split())
A = list(map(int, input().split()))

from itertools import accumulate
for i in range(k):
    imos = [0]*(n+1)
    for j in range(n):
        d = A[j]
        l = max(0, j-d)
        r = min(n-1, j+d)
        imos[l] += 1
        imos[r+1] -= 1
    imos = list(accumulate(imos))
    for j in range(n):
        A[j] = imos[j]
    if A == [n]*n:
        break

print(*A)
