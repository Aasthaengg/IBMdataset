A, B, C = map(int, input().split())
N = int(input())

print(max(A, B, C) * (2 ** N - 1) + A + B + C)