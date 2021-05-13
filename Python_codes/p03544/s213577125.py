L = [0 for _ in range(100)]
L[0], L[1] = 2, 1

N = int(input())
for i in range(2, N + 1):
    L[i] = L[i - 1] + L[i - 2]

print(L[N])