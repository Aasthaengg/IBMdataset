import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

P = {'s':R, 'p':S, 'r':P, 'N':0}

score = 0

for i in range(N):
    if i + K < N:
        if T[i] == T[i + K]:
            T[i + K] = 'N'
    
    score += P[T[i]]

print(score)