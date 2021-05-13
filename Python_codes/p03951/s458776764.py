N = int(input())
S = input()
T = input()
ren = 0
for i in range(N):
    A = S[-(i+1):]
    B = T[:(i+1)]
    if A == B:
        ren = i+1
print(2*N-ren)