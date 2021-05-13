n, k = map(int, input().split())

result = 1
for _ in range(1, n):
    result *= k - 1
print(result * k)