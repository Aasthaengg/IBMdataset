N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#累積和
sumA = [0]*(N+1)
sumB = [0]*(N+1)
for i in range(N):
    sumA[i+1] = A[i] + sumA[i]
    sumB[i+1] = B[i] + sumB[i]

ncandy = 0
for i in range(1, N+1):
    nsum = sumA[i] + (sumB[N] - sumB[i-1])
    if ncandy < nsum:
        ncandy = nsum

print(ncandy)
