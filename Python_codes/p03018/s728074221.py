s = input()
ans = 0
ds = []
tmp = 0
b = ""
while tmp < len(s):
    if s[tmp] == 'A':
        b += 'A'
        tmp += 1
    elif s[tmp:tmp+2] == "BC":
        b += 'D'
        tmp += 2
    else:
        ds.append(b)
        b = ""
        tmp += 1
ds.append(b) if b else None
ans = 0
def inver(s):
    tmp = 0
    res = 0
    for i in s:
        if i == 'A':
            tmp += 1
        else:
            res += tmp
    return res
for i in ds:
    ans += inver(i)
print(ans)