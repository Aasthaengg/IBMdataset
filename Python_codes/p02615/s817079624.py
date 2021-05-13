N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
comfortability = 0
for i in range(N):
    comfortability += A[i//2]
print(comfortability-A[0])