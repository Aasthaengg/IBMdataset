import sys
input = sys.stdin.readline
n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

D = [[0] * 3 for i in range(n)]

D[0] = A[0]
for i in range(1, n):
    for j in range(3):
        D[i][j] = max(D[i-1][(j+1)%3], D[i-1][(j+2)%3]) + A[i][j]
print(max(D[-1]))
