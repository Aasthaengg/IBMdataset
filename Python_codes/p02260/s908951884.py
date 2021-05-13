N = int(input())
A = [int(n) for n in input().split()]
cnt = 0
for i in range(N):
    min_x = A[i]
    exchange = "no"
    for j in range(i+1, N):
        if min_x > A[j]:
            min_x = A[j]
            index = j
            exchange = "ok"
    if exchange == "ok":
        A[index] = A[i]
        A[i] = min_x
        cnt += 1
for i in range(N):
    if i == N - 1:
        print(A[i])
    else:
        print(A[i], end=" ")
print(cnt)