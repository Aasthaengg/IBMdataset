s = input()
a = [s[0]]
tmp = ""
cnt = 1

for i in range(1, len(s)):
    tmp = tmp + s[i]
    if a[-1] != tmp:
        a.append(tmp)
        tmp = ""
        cnt += 1
    else:
        continue
print(cnt)
