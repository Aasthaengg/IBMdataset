N = int(input())
if N == 1:
    print(0)
    exit()
A = [int(i) for i in input().split()]
A = [A[i] - i - 1 for i in range(N)]
A.sort()
if N == 2:
    print(abs(A[0] - A[1]))
    exit()

sum_A = [0, 0]
for i in range(N):
    sum_A[0] += abs(A[i] - A[N // 2])
sum_2 = 0
for i in range(N):
    sum_A[1] += abs(A[i] - A[N // 2 + 1])
print(min(sum_A))
