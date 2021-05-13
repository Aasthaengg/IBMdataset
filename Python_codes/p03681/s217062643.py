import math

N_inu, M_saru = map(int, input().split())

d = abs(N_inu - M_saru)

if (d > 1):
    ans = 0

else:
    if (d == 1):
        ans = math.factorial(N_inu) * math.factorial(M_saru)
    else:
        ans = 2 * math.factorial(N_inu) * math.factorial(M_saru)

ans = ans % (10 ** 9 + 7)

print(ans)