# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = input()
Sset = set(S.rstrip('\n'))
# print(Sset)

n = 0
for SS in Sset:
    if S.count(SS) % 2 == 0:
        n += 1
if len(Sset) == n:
    print("Yes")
else:
    print("No")
