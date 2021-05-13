N = int(input())
ABs = [tuple(map(int, input().split())) for _ in range(N)]

A, B = min(ABs, key=lambda t: t[1])
print(A + B)