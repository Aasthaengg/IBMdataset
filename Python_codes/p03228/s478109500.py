A, B, K = [int(x) for x in input().split()]

while True:
    if A % 2 == 1:
        A -= 1
    t = A // 2
    A, B = A - t, B + t

    K -= 1
    if K <= 0:
        break

    if B % 2 == 1:
        B -= 1
    t = B // 2
    A, B = A + t, B - t

    K -= 1
    if K <= 0:
        break

print('{} {}'. format(A, B))
