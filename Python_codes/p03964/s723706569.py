import sys
input = sys.stdin.readline
N = int(input())
T = []
A = []
for i in range(N) :
    p, q = map(int,input().split())
    T.append(p)
    A.append(q)

Tak = T[0]
Aok = A[0]
for i in range(1, N) :
    Tb = (Tak + T[i] - 1) // T[i]
    Ab = (Aok + A[i] - 1) // A[i]
    Tak = T[i] * max(Tb, Ab)
    Aok = A[i] * max(Tb, Ab)

print(Tak + Aok)
