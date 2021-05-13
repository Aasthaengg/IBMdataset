a, b, c = map(int, input().split())
ans = 0
if a == b == c:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        pass
    else:
        ans = -1
else:
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        ans += 1
        a, b, c = (b+c)//2, (a+c)//2, (a+b)//2
print(ans)
