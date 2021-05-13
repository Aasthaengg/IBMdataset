# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
n = 0
i = A
while i <= B:
    L = list(str(i))
    if L[0] == L[4] and L[1] == L[3]:
        n += 1
    i += 1
print(n)
