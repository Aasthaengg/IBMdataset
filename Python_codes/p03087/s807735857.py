N, Q = map(int,input().split())
S = input()
T = [0]*(N+1)
for i in range(N):
    T[i+1] = T[i] + (1 if S[i : i+2] == 'AC' else 0)

for i in range(Q):
    L, R = map(int,input().split())
    print(T[R-1] - T[L-1])