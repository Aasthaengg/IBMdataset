S = int(input())
N = int(1e9)
x = N - (S - 1) % N - 1
y = (S - 1) // N + 1
print(0, 0, N, 1, x, y)