N, A, B = map(int, input().split())

MIN = A * (N - 1) + B
MAX = B * (N - 1) + A

print (max(0, MAX - MIN + 1))