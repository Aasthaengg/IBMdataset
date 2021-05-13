from fractions import gcd


N, M = map(int, input().split(" "))
S = input()
T = input()
a, b = M // gcd(N, M), N // gcd(N, M)
GCD = gcd(N, M)

flag = True
for n in range(0, GCD):
    flag &= S[b * n] == T[a * n]

if flag:
    print(N * M // GCD)
else:
    print(-1)