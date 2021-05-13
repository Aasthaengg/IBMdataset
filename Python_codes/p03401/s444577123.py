N = int(input())
A = list(map(int, input().split()))
A.append(0)

total = 0
now = 0
skip = {}

for i in range(N):
    total += abs(A[i] - now)
    skip[i] = abs(A[i+1] - now) - abs(A[i] - now) - abs(A[i+1] - A[i])
    now = A[i]
total += abs(now)

for i in range(N):
    # print(total, skip[i])

    print(total+skip[i])