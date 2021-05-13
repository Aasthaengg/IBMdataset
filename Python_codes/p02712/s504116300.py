N = int(input())
S = sum(i for i in range(1, N + 1) if not (i % 3 == 0 or i % 5 == 0))
print(S)
