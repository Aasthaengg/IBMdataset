s = input()

cnt = 0
tmp = ''
cnd = ''

for i in range(len(s)):
    cnd += s[i]
    if cnd != tmp:
        tmp = cnd
        cnt += 1
        cnd = ''
print(cnt)