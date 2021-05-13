n, k = map(int, input().split())

even = n // k
odd = (n + k//2) // k

res = even ** 3
if k % 2 == 0:
    res += odd ** 3

print(res)

# Sent from my iPhone