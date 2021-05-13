import math
N, M = map(int, input().split())
S = list(input())
T = list(input())
lcm = (N * M) // math.gcd(N, M)
ans = lcm
Sp = lcm//N
Tp = lcm//M
lcmlcm = (Sp * Tp) // math.gcd(Sp, Tp)
owari = min(Sp*N, M*Tp)
for i in range(0, owari, lcmlcm):
    if S[i//Sp] != T[i//Tp]:
        ans = -1
        break
print(ans)
