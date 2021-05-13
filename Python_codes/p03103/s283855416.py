N, M = map(int, input().split())

A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

c = zip(A, B)
c = sorted(c)

A, B = zip(*c)

count = 0
money = 0
for i in range(N):
    count += B[i]
    money += A[i] * B[i]
    if count < M:
        continue
    else:
        while count != M:
            count -= 1
            money -= A[i]
        print(money)
        exit()
