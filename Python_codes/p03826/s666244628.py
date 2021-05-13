def actual(A, B, C, D):
    area1 = A * B
    area2 = C * D

    if area1 >= area2:
        return area1

    return area2

A, B, C, D = map(int, input().split())
print(actual(A, B, C, D))