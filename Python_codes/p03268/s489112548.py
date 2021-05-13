N, K = map(int, input().split())

total = 0
total += (N // K)**3

if K % 2 == 0:
    K //= 2
    n = N // K
    n = n // 2 + n % 2
    total += n**3

print(total)