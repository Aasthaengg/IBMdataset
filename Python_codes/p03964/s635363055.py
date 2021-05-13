N = int(input())
t, a = 0, 0
for _ in range(N):
    T, A = map(int, input().split())
    c = max((t - 1) // T + 1, (a - 1) // A + 1)
    t = T * c
    a = A * c
    if t + a == 0:
        t += T
        a += A
    # for n in range(10 ** 18):
    #     if t <= n * T and a <= n * A:
    #         t = n * T
    #         a = n * A
    #         print('{0} {1} {2}'.format(n, t, a))
    #         break
print(int(t + a))