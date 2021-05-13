N, K = map(int, input().split())
A_array = list(map(int, input().split()))
F_array = list(map(int, input().split()))

A_array.sort()
F_array.sort()
F_array = F_array[::-1]

X = 0
Y = 10 ** 12

while(Y - X > 0):
    mid = (X + Y) // 2
    k = 0
    for a, f in zip(A_array, F_array):
        m = mid // f
        # print(a, f, k)
        k += max(0, a - m)
    if k <= K:
        Y = mid
    else:
        if Y - X == 1:
            break
        X = mid

print(Y)
