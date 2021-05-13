N, M = map(int, input().split())
S = input()
T = input()


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


n_lcm = lcm(len(S), len(T))
gcd_nm = gcd(N, M)

s_step = N // gcd_nm
t_step = M // gcd_nm

for i in range(gcd_nm):
    if S[i * N // gcd_nm] != T[i * M // gcd_nm]:
        print(-1)
        exit()
print(n_lcm)

