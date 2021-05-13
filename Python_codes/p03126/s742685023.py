# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LikeL = []
for i in range(N):
    temp = list(map(int, input().split()))
    temp.pop(0)
    LikeL.append(temp)

ans = 0
for Mi in range(M):
    all = True
    for i in range(N):
        if not(Mi+1 in LikeL[i]):
            all = False
            break
    if all:
        ans += 1
print(ans)
