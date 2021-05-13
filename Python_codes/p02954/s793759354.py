s = input()
n = len(s)

l = []
length = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        length += 1
    else:
        l.append([i, length])
        length = 1
l.append([i+1, length])

res = [0] * n
for i in range(0, len(l), 2):
    if l[i][1] % 2 == 1:
        res[l[i][0]] = (l[i][1] + l[i+1][1] + 1) // 2
        res[l[i][0]+1] = (l[i][1] + l[i+1][1]) // 2
    else:
        res[l[i][0]] = (l[i][1] + l[i+1][1]) // 2
        res[l[i][0]+1] = (l[i][1] + l[i+1][1] + 1) // 2

for v in res:
    print(v, end=" ")