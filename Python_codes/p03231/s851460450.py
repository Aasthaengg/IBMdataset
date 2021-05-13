def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


N, M = map(int, input().split())
S = input()
T = input()
x = gcd(N, M)
n = N // x
m = M // x

for i in range(x):
    if S[n*i] != T[m*i]:
        print(-1)
        exit()
print(N*M//x)
