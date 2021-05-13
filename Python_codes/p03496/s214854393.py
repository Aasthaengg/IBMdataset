N = int(input())
a = list(map(int, input().split()))
max_a = max(a)
min_a = min(a)
print(2 * N - 1)
if abs(max_a) >= abs(min_a):
    for i in range(1, N + 1):
        print(a.index(max_a) + 1, i)
    for i in range(1, N):
        print(i, i + 1)
else:
    for i in range(1, N + 1):
        print(a.index(min_a) + 1, i)
    for i in range(N, 1, -1):
        print(i, i - 1)