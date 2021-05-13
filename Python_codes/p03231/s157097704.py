import fractions
N, M = map(int, input().split())
S = input()
T = input()
f = fractions.gcd(N, M)
flag = True
for i in range(f):
    if S[i*N//f] != T[i*M//f]:
        flag = False
        break
print([-1,N*M//f][flag])