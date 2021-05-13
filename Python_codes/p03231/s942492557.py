from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()
GCD = gcd(N, M)
LCM = N*M // gcd(N, M)
# print(GCD, LCM)
ok = True
for i in range(GCD):
    # print(i*N//GCD, i*M//GCD)
    if S[i*(N//GCD)] != T[i*(M//GCD)]:
        ok = False

if ok:
    print(LCM)
else:
    print(-1)
