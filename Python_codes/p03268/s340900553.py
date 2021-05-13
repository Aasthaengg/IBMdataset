N, K = map(int, input().split(' '))

# 1
n = N // K
ret = n ** 3

# 2
if not K % 2:
    m = K // 2
    n = len(list(range(m, N+1, K)))
    ret += n ** 3

print(ret)


