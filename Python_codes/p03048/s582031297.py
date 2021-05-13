# 2020/07/26
# diverta 2019 Programming Contest - B

# Input
r, g, b, n = map(int,input().split())

ans = 0

# Calc
for ir in range(n+1):
    vr = r * ir 
    if vr > n:
        break

    for ig in range(n+1):
        vg = g * ig 
        if vg + vr > n:
            break
        cb = n - vr - vg
        if cb % b == 0:
            ans = ans + 1

# Output
print(ans)
