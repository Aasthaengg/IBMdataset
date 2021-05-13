N_gyou, M_retu = map(int, input().split())

if (N_gyou == 2 or M_retu == 2):
    ans = 0
elif (N_gyou == 1 and M_retu == 1):
    ans = 1
elif (N_gyou == 1):
    ans = M_retu - 2
elif (M_retu == 1):
    ans = N_gyou - 2
else:
    ans = (N_gyou - 2) * (M_retu - 2)

print(ans)