# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
list_V = list(map(float, input().split()))
list_V.sort()

n = 0.0
while len(list_V) >= 2:
    list_V.sort()
    n = (list_V[0] + list_V[1])/2
    list_V.append(n)
    list_V.pop(0)
    list_V.pop(0)

print(list_V[0])
