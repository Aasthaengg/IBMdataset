from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()
flg = True

ans = N*M//gcd(N, M)
n = ans // N
m = ans // M
a = n*m//gcd(n, m)
nn = a // n
mm = a // m
for i in range(1, ans//a):
    if S[nn*i] != T[mm*i]:
        flg = False
if S[0] != T[0]:
    flg = False
if flg:
    print(ans)
else:
    print(-1)