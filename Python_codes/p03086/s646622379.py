def checkACGT(s):
    ss = ''.join(s)
    check = ss.replace('A', '').replace('C', '')\
    .replace('G','').replace('T', '')
    if len(check) == 0:
        return True
    else:
        return False


s = input()
ans = 0
for i in range(len(s)):
    for j in range(len(s) - i + 1):
        ss = s[i:j + i]
        # print(ss)
        if (checkACGT(ss)):
            ans = max(ans, len(ss))
print(ans)
