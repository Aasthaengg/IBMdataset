import fractions
N,M =list(map(int,input().split(" ")))
S = input()
T = input()
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

ans = lcm(N,M)

step_S = ans //M
step_T = ans //N

ind_s = 0
ind_t = 0
while True:

    if ind_s >= N or ind_t >= M:
        break

    if S[ind_s ] != T[ind_t]:
        print(-1)
        exit(0)

    ind_s += step_S
    ind_t += step_T
print(ans)