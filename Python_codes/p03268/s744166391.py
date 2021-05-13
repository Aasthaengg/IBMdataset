N, K = map(int, input().split())

if K % 2 == 1:
    ans = (N // K) ** 3
else:
    a = N // K
    b = 0
    for i in range(1, N+1):
        if i % K == K // 2:
            b += 1
    ans = a ** 3 + b ** 3

print(ans)