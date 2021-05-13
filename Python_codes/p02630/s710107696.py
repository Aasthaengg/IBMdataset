import sys
input = sys.stdin.buffer.readline

n = int(input())
A = list(map(int, input().split()))
S = sum(A)

D = [0]*(10**5+1)
for a in A:
    D[a] += 1

q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    S -= D[b]*b
    S += D[b]*c
    D[c] += D[b]
    D[b] = 0
    print(S)
