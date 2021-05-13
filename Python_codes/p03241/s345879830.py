n, m = map(int, input().split())
result = 1
for i in range(int(m**0.5), 0, -1):
    if m % i == 0:
        j = m // i
        if i >= n:
            result = max(result, j)
        elif j >= n:
            result = max(result, i)
print(result)
