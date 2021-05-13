s = list(input())
l = [-1]
i = 0

while i < len(s):
    if s[i] == "<":
        l.append(l[i] + 1)
    if s[i] == ">":
        cnt = 0
        while s[i + cnt] == ">":
            if i + cnt == len(s) -1:
                cnt += 1
                break
            cnt += 1
        if l[i] < cnt:
            l.append(cnt)
        else:
            l.append(l[i] + 1)
        i += cnt
        cnt -= 1
        while cnt != -1:
            l.append(cnt)
            cnt -= 1
    i += 1
if s[len(s) -1] == "<":
    l.append(l[i] + 1)
del l[0]
ans = sum(l)
print(ans)