N, A, B = map(int, input().split())
max_value = (N - 1) * B + A
min_value = (N - 1) * A + B

if max_value >= min_value:
    print(max_value - min_value + 1)
else:
    print(0)
