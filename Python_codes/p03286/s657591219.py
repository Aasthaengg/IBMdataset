n = int(input())

cnt = 0
ans = ""
while n != 0:
    if n % 2 == 0:
        ans = "0" + ans
    else:
        ans = "1" + ans
        if cnt % 2 == 0:
            n -= 1
        else:
            n -= -1
    cnt += 1
    n //= 2
if len(ans) == 0:
    ans = "0"
print(ans)