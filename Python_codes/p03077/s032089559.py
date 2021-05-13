n = int(input())
L = [int(input()) for _ in range(5)]
print((n + min(L) - 1) // min(L) + 4)
