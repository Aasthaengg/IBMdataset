N, A, B = map(int, input().split())

d = N - (A + B)
print(min(A, B), -d if d < 0 else 0)
