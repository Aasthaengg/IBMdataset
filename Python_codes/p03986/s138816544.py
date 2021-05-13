s = input()
ans = 0
cnt = 0
for i in s:
    if i == "S":
        cnt += 1
    else:
        if cnt:
            ans += 1
            cnt -= 1
print(len(s) - (2*ans))