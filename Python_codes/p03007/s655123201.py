N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)

P = [a for a in A if a >= 0]
Q = [a for a in A if a < 0]

if len(P) == 0:
    P = [A[0]]
    Q = A[1:]
if len(Q) == 0:
    P = A[:-1]
    Q = [A[-1]]

print(sum(P) - sum(Q))

for i in range(1, len(P)):
    print(Q[0], P[i])
    Q[0] -= P[i]

for i in range(1, len(Q)):
    print(P[0], Q[i])
    P[0] -= Q[i]

print(P[0], Q[0])