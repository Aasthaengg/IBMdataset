n, k = map(int, input().split())
A = [0] * (10 ** 5 + 10)
for _ in range(n):
    a, b = map(int, input().split())
    A[a] += b
cnt = 0
for i in range(10 ** 5 + 10):
    cnt += A[i]
    if cnt >= k:
        print(i)
        exit()