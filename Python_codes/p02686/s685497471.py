
N = int(input())
X = [input() for _ in range(N)]

ctr = [[], []]
for s in X:
    t = [0] * (len(s) + 1)
    for j in range(len(s)):
        t[j + 1] = t[j] + int(s[j] == "(") - int(s[j] == ")")

    if t[-1] > 0:
        ctr[0].append((min(t), t[-1]))
    else:
        ctr[1].append((min(t) - t[-1], -t[-1]))

flag = True
tmp = 0
for i in range(2):
    cur = 0
    for m, c in sorted(ctr[i], reverse=True):
        flag &= cur + m >= 0
        cur += c

    if i == 0:
        tmp = cur
    else:
        flag &= tmp == cur

if flag:
    print("Yes")
else:
    print("No")
