from math import gcd

N, M = map(int, input().split())
S = input()
T = input()

x = gcd(N, M)
n = N//x
m = M//x
for i in range(x):
    if S[n*i] != T[m*i]:
        print(-1)
        break
else:
    print(N*M//x)