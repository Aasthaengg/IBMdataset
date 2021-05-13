N, K= (int(x) for x in input().split(' '))

if K % 2 == 1:
    print((N // K) ** 3)
else:
    print((N // K) ** 3 + (int(N - K // 2) // K + 1) ** 3)

