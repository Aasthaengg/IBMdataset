s = input()
cnt = 1
now = s[0]
tmp = ''
for s in s[1:]:
    tmp += s
    if now != tmp:
        cnt+=1
        now = tmp
        tmp = ''
print(cnt)