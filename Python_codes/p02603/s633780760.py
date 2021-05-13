N = int(input())
A = list(map(int, input().split()))

i = 0

yen = 1000
while i < N:
    while i < N - 1 and A[i] >= A[i + 1]:
        i += 1

    if i == N - 1:
        break

    x = i
    while i < N - 1 and A[i] <= A[i + 1]:
        i += 1

    y = i

    cnt = yen // A[x]
    yen = yen - A[x] * cnt + A[y] * cnt

print(yen)