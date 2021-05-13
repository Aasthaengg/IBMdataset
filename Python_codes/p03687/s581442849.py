from collections import Counter
s = input()
c = Counter(s)
ans = float("inf")
for i in c.keys():
    s2 = list(s)
    cnt = 0
    while s2:
        if len(set(s2)) == 1:
            break
        for j in range(len(s2) - 1):
            if s2[j] == i or s2[j + 1] == i:
                s2[j] = i
            else:
                continue
        s2 = s2[:-1]
        cnt += 1
    ans = min(ans, cnt)
print(ans)