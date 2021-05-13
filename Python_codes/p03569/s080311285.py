s = input()
cnt = 0
while len(s) > 0:
    if s[0] == s[-1]:
        s = s[1:-1]
    else:
        if s[0] == "x":
            cnt += 1
            s = s[1:]
        elif s[-1] == "x":
            cnt += 1
            s = s[:-1]
        else:
            cnt = -1
            break
print(cnt)