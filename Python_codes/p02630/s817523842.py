N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = []
C = []
for i in range(Q):
    b,c = map(int,input().split())
    B.append(b)
    C.append(c)
S = sum(A)
NUM = [0] * 100005
for a in A:
    NUM[a] += 1
for k in range(Q):
    S += (C[k]-B[k]) * (NUM[B[k]])
    NUM[C[k]] += NUM[B[k]]
    NUM[B[k]] = 0
    print(S)

