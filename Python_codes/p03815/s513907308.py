n = int(input())

ans = 2*(n // 11)
if n % 11 > 6:
    ans += 2
elif n % 11 > 0:
    ans += 1
else:
    ans += 0

print(ans)