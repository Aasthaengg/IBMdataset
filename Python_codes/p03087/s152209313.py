N, Q = map(int, input().split())
S = ['0'] + list(input())
C = [0] * len(S)
c = 0
for i in range(1, len(S)):
    if S[i-1] == "A" and S[i] == "C":
        c += 1
    C[i] = c
for _ in range(Q):
    l, r = map(int, input().split())
    print(C[r] - C[l])
