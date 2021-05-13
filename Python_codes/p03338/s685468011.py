n = int(input())
s = input()
M = 0
for i in range(1, n):
    cnt = 0
    s1 = s[:i]
    s2 = s[i:]
    t = {}
    for x in s1:
        if x not in t: t[x]=1
    for k in s2:
        if k not in t: t[k]=0
        if t[k] == 1: t[k]+=1
    for x, y in t.items():
        if y==2: cnt+=1
    M = max(cnt, M)
print(M)