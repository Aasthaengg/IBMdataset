N, A, B = map(int, input().split())

sum_min = A * (N - 1) + B
sum_max = A + B * (N - 1)

print(max(0, sum_max - sum_min + 1))