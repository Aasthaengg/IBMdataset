N = int(input())

result = 0
for i in range(1, N+1):
    m = N // i - 1
    if m == 0:
        continue
    if N // m == N % m:
        result += m
    elif m < i:
        break

print(result)
