A, B, C, D = tuple(int(input()) for _ in range(4))

train = min(A, B)
bus = min(C,D)
print(train+bus)