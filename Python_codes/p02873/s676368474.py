s = input()

cnt = 0
ans = 0
tmp = 0
check = 0
for x in s:
    cnt += 1
    if x == '<':
        if check != cnt - 1:
            ans -= tmp * (cnt - check - 1)
            tmp = 0
        tmp += 1
        ans += tmp
        check = cnt
    else:
        tmp -= 1
        ans += tmp
        if tmp < 0:
            ans += (cnt -  check + 1)
            tmp += 1

print(ans)
