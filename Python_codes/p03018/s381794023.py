s = input()
ans = 0
tmp = 0
i = 0
while i < len(s)-1:
    if s[i] == "A":
        tmp += 1
    elif s[i] == "B":
        if s[i+1] == "C":
            ans += tmp
            i += 1
        else:
            tmp = 0
    else:
        tmp = 0
    i += 1
print(ans)