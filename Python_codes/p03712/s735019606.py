# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
pic = [['#' for i in range(W+2)] for j in range(H+2)]

for i in range(H):
    S = input()
    for j in range(W):
        S1 = S[j]
        pic[i+1][j+1] = S1

for i in range(H+2):
    for j in range(W+2):
        print(pic[i][j], end="")
    print('', end='\n')
