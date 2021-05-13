N = int(input())
A = []
for i in range(N):
    S, P = map(str, input().split())
    P = int(P)
    A.append([S, -P])
S = sorted(A)
for j in S:
    print(A.index(j) + 1)