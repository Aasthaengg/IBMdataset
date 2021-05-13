N, K = list(map(int, input().split()))

a, b = divmod(N, K)

if K == 1:
    print('0')
else:
    result = min(N, b, abs(K - b))
    print(result)