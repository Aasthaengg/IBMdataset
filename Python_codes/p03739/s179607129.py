N = int(input())
A = list(map(int, input().split()))

res1 = 0
cum1 = 0

for i in range(N):
    cum1 += A[i]
    if i % 2 == 0 and cum1 <= 0:
        res1 += - cum1 + 1
        cum1 = 1
    if i % 2 != 0 and cum1 >= 0:
        res1 += cum1 + 1
        cum1 = -1

res2 = 0
cum2 = 0

for i in range(N):
    cum2 += A[i]
    if i % 2 != 0 and cum2 <= 0:
        res2 += - cum2 + 1
        cum2 = 1
    if i % 2 == 0 and cum2 >= 0:
        res2 += cum2 + 1
        cum2 = -1

print(min(res1, res2))