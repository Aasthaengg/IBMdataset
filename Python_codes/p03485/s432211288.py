import math

def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

# n = int(input())
# a, b = list(map(int, input().split()))
# s = input()

a, b = list(map(int, input().split()))
ans = math.ceil((a + b) / 2)
print(ans)
