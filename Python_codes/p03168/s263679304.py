import sys
input = sys.stdin.readline

n = int(input())
P = list(map(float,input().split()))

D = [[0] * (n+1) for i in range(n+1)]
D[0][0] = 1
for i in range(1, n+1):
    for j in range(n+1):
        D[i][j] = D[i-1][j] * P[i-1]
        if j-1 >= 0:
            D[i][j] += D[i-1][j-1] * (1-P[i-1])

print(sum(D[-1][:(n+1)//2]))