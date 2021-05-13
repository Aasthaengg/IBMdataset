def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


N, M = map(int, input().split())
S = input()
T = input()
gcd_val = gcd(N, M)
for i in range(gcd_val):
    if S[i * N // gcd_val] != T[i * M // gcd_val]:
        print(-1)
        exit()
print(lcm(N, M))
