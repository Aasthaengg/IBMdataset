# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())

if A > B:
    print("GREATER")
elif B > A:
    print("LESS")
else:
    print("EQUAL")
