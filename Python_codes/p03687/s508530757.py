s = input()
ans = len(s)
for c in set(s):
    new_s = s
    while len(set(new_s)) > 1:
        tmp = ""
        for i in range(len(new_s) - 1):
            tmp += c if new_s[i] == c or new_s[i + 1] == c else new_s[i]
        new_s = tmp
    ans = min(ans, len(s) - len(new_s))
print(ans)
