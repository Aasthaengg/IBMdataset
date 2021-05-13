s = input()

ans = 0
cnt = 0
for i in s:
    if i == "g":
        if cnt >= 1:
            cnt -= 1
            ans += 1
        else:
            cnt += 1
    else:
        if cnt >= 1:
            cnt -= 1
        else:
            cnt += 1
            ans -= 1

print(ans)