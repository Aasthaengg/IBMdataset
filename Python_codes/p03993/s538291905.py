# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[A[i] - 1] - 1 == i:
        ans += 1
print(ans//2)
