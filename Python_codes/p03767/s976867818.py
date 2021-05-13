N = int(input())
A = list(map(int, input().split()))
sort_A = sorted(A, reverse=True)
sumA = 0
# print(sort_A)
for x in range(N):
    sumA += sort_A[2 * x + 1]
print(sumA)
