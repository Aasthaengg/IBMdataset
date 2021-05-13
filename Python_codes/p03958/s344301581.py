K, T = map(int, input().split())
A = list(map(int, input().split()))

maxix = 0
maxv = -1

for aix in range(T):
    if A[aix] > maxv:
        maxv = A[aix]
        maxix = aix

total = 0
for aix in range(T):
    if aix == maxix:
        continue
    else:
        total += A[aix]

if maxv - 1 > total:
    print(maxv-total-1)
else:
    print(0)

