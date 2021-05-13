N, A, B =list(map(int, input().split()))

MAX = min(A, B)

MIN = max(0,A+B-N)

print(MAX,MIN)