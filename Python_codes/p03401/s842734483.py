N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)
my_sum = 0
for i in range(1, N + 2):
    my_sum += abs(A[i] - A[i - 1])
for i in range(1, N + 1):
    if A[i - 1] <= A[i] <= A[i + 1] or A[i + 1] <= A[i] <= A[i - 1]:
        print(my_sum)
    elif A[i + 1] <= A[i - 1] <= A[i] or A[i] <= A[i - 1] <= A[i + 1]:
        print(my_sum - 2 * abs(A[i] - A[i - 1]))
    elif A[i - 1] <= A[i + 1] <= A[i] or A[i] <= A[i + 1] <= A[i - 1]:
        print(my_sum - 2 * abs(A[i] - A[i + 1]))