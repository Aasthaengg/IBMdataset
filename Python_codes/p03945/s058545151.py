s = list(input())

cnt = 0
check = ""

for i in range(len(s)):
    if check == "":
        check = s[i]
        continue

    if check == s[i]:
        continue
    else:
        check = s[i]
        cnt += 1


print(cnt)