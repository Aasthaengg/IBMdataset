import sys
input = sys.stdin.readline

S = list(input().rstrip('\n'))
K = int(input())

n = 1
for i in range(min(len(S), K)):
    if S[i] != '1':
        n = int(S[i])
        break
print(n)
