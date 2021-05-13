x = int(input())
ans = 0
if x <= 6: print(1)
else:
    ans = x // 11
    ans *= 2
    x %= 11
    if x == 0: print(ans)
    elif x <=6: print(ans+1)
    else: print(ans+2)