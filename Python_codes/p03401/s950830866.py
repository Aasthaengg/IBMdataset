N = int(input())
A = list(map(int, input().split()))
pre = 0
sumall = 0

for i in range(N):
   sumall += abs(A[i] - pre)
   pre = A[i]

sumall += abs(A[i])
pre = 0
for i in range(N-1):
    ans = sumall - abs(A[i] -pre) - abs(A[i+1] - A[i]) + abs(A[i+1] -pre)
    pre = A[i]
    print(ans)
print(sumall - abs(A[N-1] -A[N-2]) - abs(A[N-1]) + abs(A[N-2]))   