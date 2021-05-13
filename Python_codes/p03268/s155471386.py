N, K = [int(i) for i in input().split()]

count = (N // K) ** 3
if K % 2 == 0:
    count += ((N - (K // 2)) // K + 1) ** 3

print(count)