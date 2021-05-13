a,b = map(int, input().split())
ans = abs(abs(a) - abs(b))
sign = inc = 0
if a*b < 0:
    sign = 1
if a-b < 0:
    inc = 1

if a==0 and b==0:
    print(0)
    exit()
elif a==0:
    if inc == 0:
        ans += 1
        print(ans)
        exit()
elif b==0:
    if inc == 0:
        ans += 1
        print(ans)
        exit()

if sign == 0 and inc == 0:
    ans += 2
elif sign == 0 and inc == 1:
    pass
else:
    ans += 1
print(ans)