N = int(input())
print(sum(N // n - 1 for n in range(1, int(N ** 0.5) + 1) if not N % n and n < N // n - 1))