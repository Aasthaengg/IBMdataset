s = list(str(input()))

if len(set(s)) == 1:
    print(0)
    exit()

import copy
ans = 101
for i in range(26):
    c = chr(i+ord('a'))
    t = copy.copy(s)
    cnt = 0
    while True:
        temp = []
        cnt += 1
        for j in range(len(t)-1):
            if t[j] == c:
                temp.append(t[j])
            elif t[j+1] == c:
                temp.append(t[j+1])
            else:
                temp.append(t[j])
        t = copy.copy(temp)
        if len(set(t)) == 1:
            break
    ans = min(ans, cnt)
print(ans)
