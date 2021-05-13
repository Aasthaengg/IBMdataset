import math
s = list(input())
ss = s[:]
k = int(input())
cnt = 0

if len(set(s)) == 1:
    cnt = math.floor(len(s) * k / 2)
else:
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
            s[i + 1] = '*'
    cnt *= k
    if ss[0] == ss[-1]:
        a = 1
        for i in range(len(ss) - 1):
            if ss[i] == ss[i + 1]:
                a += 1
            else:
                break
        b = 1
        for j in range(len(ss) - 1, 0, -1):
            if ss[j] == ss[j - 1]:
                b += 1
            else:
                break
        cnt -= (k - 1) * (math.floor(a / 2) + math.floor(b / 2) - math.floor((a + b) / 2))
print(cnt)