# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A, B, C, K = map(int, input().split())

if abs(A - B) > 10 ** 18:
    print("Unfair")
elif K % 2 == 0:
    print(A-B)
else:
    print(B-A)
