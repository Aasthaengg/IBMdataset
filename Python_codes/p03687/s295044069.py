s = input()
l = {}
for i in s:
    l.setdefault(i, 0)
    l[i] += 1
ans = float("inf")
for i in l.keys():
    count = 0
    s0 = ""
    for j in s:
        if i == j:
            s0 += i
        else:
            s0 += "."
    while "." in s0:
        count += 1
        s1 = ""
        for j in range(len(s0) - 1):
            if s0[j] == i or s0[j + 1] == i:
                s1 += i
            else:
                s1 += "."
        s0 = s1
    else:
        ans = min(ans, count)
print(ans)