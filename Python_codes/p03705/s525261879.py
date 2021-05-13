N, A, B = map(int, input().split())

small = A * N + (B - A)
big = B * N - (B - A)
ans = big - small + 1

print(ans if ans > 0 else 0)