N = int(input())

if N % 2 == 0:
    result = N // 2
    result = result * (N - 1)
elif N % 2 == 1:
    result = (N - 1) // 2
    result = result * N

print(result)
