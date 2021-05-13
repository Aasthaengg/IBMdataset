N,Q = (int(X) for X in input().split())
S = input()
T = [0]*(N+1)
for I in range(0,N):
     T[I+1] = T[I] + (S[I:I+2]=='AC')
for J in range(0,Q):
    L,R = (int(X)-1 for X in input().split())
    print(T[R]-T[L])