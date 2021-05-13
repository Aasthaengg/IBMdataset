n = int(input())
check = 2
ans =""
if n == 0:
    print(0)
    exit()
while n != 0:
    if n% 2 != 0:
        n -= 1
        ans = "1"+ans
    else:
        ans = "0" + ans
    n //= -2
print(ans)
