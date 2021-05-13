def actual(N):
    for i in range(N, 0, -1):
        is_square_number = (i ** 0.5) % 1 == 0

        if is_square_number:
            return i

N = int(input())
print(actual(N))