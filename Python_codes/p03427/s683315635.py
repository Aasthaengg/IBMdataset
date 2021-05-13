# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import math
import sys
input = sys.stdin.readline

N = int(input())
ans = 0
k = int(math.log10(N)) + 1
A = N//(10**(k-1))
if (A + 1) * (10 ** (k - 1)) - 1 <= N:
    ans = A + 9*(k-1)
else:
    ans = A-1+9*(k-1)
print(ans)
