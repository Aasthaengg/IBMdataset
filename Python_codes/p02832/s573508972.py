# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

n = 1
ans = 0
for i in A:
    if i == n:
        n += 1
    else:
        ans += 1
if n == 1:
    print(-1)
else:
    print(ans)
