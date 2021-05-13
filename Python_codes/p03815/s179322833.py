n = int(input())
ans = 0
ans += 2*(n // 11)
n %= 11
if n >= 7:
    print(ans+2)
elif n >= 1:
    print(ans+1)
else:
    print(ans)