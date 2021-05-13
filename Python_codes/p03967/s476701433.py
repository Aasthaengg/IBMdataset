s = input()
at = 0
to = 0
res = 0

for i in s:
    if i == "g":
        to += 1
        if at > 0:
            at -= 1
            res += 1
        else:
            at += 1
    elif i == "p":
        to -= 1
        if at > 0:
            at -= 1
        else:
            at += 1
            res -= 1
else:
    print(res)
