s = input()

cnt = 1
pre = s[0]
i = 1
while i < len(s):
    if i == len(s)-1 and s[i] == pre:
        break
    elif s[i] == pre:
        pre = s[i:i+2]
        i += 2
        cnt += 1
    else:
        pre = s[i]
        i += 1
        cnt += 1

print(cnt)