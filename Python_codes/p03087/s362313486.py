N, Q = map(int, input().split())
S = input()

C = [0]*N
for i in range(1, N):
    C[i] += C[i-1]
    if(S[i-1:i+1] == 'AC'):
        C[i] += 1

for i in range(Q):
    l, r = map(int, input().split())
    print(C[r-1]-C[l-1])
