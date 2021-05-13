A, B, C = map(int, input().split())

BC = min(B, C)
B -= BC
C -= BC

if C > 0:
    if A >= C:
        ans = BC * 2 + C
    else:
        ans = BC * 2 + A + 1
else:
    ans = BC*2+B


print(ans)
