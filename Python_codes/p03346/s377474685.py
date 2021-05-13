import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())

P = [int(input()) for i in range(N)]

T = [0]*(N-1)

E = [0]*N

for i in range(N):
    E[P[i]-1] = 1
    if P[i]<N:
        if E[P[i]]==1:
            T[P[i]-1] = 1

max_score = 0
prev = -1

for i in range(N-1):
    if T[i]==1:
        max_score=max(max_score,i-prev)
        prev = i

max_score = max(max_score,N-1-prev)

print(N-max_score)