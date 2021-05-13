N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
sumVC = 0
for x in range(N):
    if V[x] - C[x] > 0:
        sumVC += V[x] - C[x]
print(sumVC)
