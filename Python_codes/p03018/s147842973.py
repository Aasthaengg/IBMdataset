s = list(input())
t = []
ls = len(s)
for i in range(ls):
    if s[i] == "A":
        t.append("A")
    elif s[i] == "B":
        if not i == ls - 1:
            if s[i + 1] == "C":
                t.append("D")
            else:
                t.append("B")
    else:
        if not i == 0:
            if not s[i - 1] == "B":
                t.append("C")
t = "".join(t).split("B")
for u in range(len(t)):
    t[u] = t[u].split("C")
ans = 0
for u in t:
    for v in u:
        dcnt = 0
        v = list(v)
        for i in range(len(v)):
            if v[i] == "D":
                ans += (i - dcnt)
                dcnt += 1
print(ans)