# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = list(input().rstrip('\n'))
T = list(input().rstrip('\n'))

n = len(S)
for i in range(n):
    SS = S[i:] + S[:i]
    if SS == T:
        print("Yes")
        exit()
print("No")
