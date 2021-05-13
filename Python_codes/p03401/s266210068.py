N = int(input())
A = [0] + list(map(int, input().split())) + [0]

all = 0
for i in range(1, N + 2):
    all += abs(A[i] - A[i - 1])

for i in range(1, N + 1):
    tmp = all
    tmp -= abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i])
    tmp += abs(A[i + 1] - A[i - 1])
    print(tmp)
