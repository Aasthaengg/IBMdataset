N = int(input())
A = list(map(int, input().split()))
countUp = 0
sumA = sum(A)
minA = 2020202020 * N
for x in range(N):
    countUp += A[x]
    sumA -= A[x]
    minA = min(minA, abs(countUp - sumA))
print(minA)
