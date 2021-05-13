N,K = map(int, input().split())

count = 0

count += (N // K) ** 3
if K % 2 == 0:
    K2 = K // 2
    count += ((N-K2) // K + 1) ** 3

print(count)
