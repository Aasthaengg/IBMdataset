s = input()

a = [[] for i in range(26)]

l = len(s)

for i in range(l):
    a[ord(s[i]) - 97].append(i)
ans = 1000

for i in range(26):
    a[i].append(l)
    t = a[i][0]
    for j in range(1, len(a[i])):
        t = max(t, a[i][j] - a[i][j-1] - 1)
    ans = min(ans, t)

print(ans)