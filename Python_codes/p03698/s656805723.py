# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = input()
Sset = set(S)
# print(Sset)
if len(S) == len(Sset):
    print("yes")
else:
    print("no")
