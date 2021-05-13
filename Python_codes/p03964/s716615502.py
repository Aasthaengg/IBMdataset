N = int(input())


def ceil(a, b):
    return (a + b - 1) // b


T, A = 1, 1
for _ in range(N):
    Tt, At = map(int, input().split())
    x = max(ceil(T , Tt), ceil(A , At))
    T, A = Tt * x, At * x
print(T + A)
