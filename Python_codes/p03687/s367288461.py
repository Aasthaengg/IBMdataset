from collections import Counter
s = input()
c = Counter(s)
ans = float("inf")
for i in c.keys():
    t = list(s)
    while t != [i]*len(t):
        u = []
        for j in range(len(t)-1):
            if t[j] == i or t[j+1] == i:
                u.append(i)
                continue
            u.append(t[j])
        t = u
    ans = min(ans,len(s)-len(t))
print(ans)