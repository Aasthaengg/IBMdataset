from collections import deque

N = int(input())
S, T = input().split()

char = deque()

for i in range(N):
    char.append(S[i])
    char.append(T[i])

print(*char, sep='')
