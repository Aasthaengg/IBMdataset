n, k = list(map(int, input().split(' ')))
s = input().strip()

t = []
c = '0'
v = 0
for i in range(n):
    if c != s[i]:
        t.append(v)
        v = 1
        c = s[i]
    else:
        v += 1
t.append(v)

r = 0
temp = 0
result = 0
for l in range(0, len(t), 2):
    while (r - l) // 2 + 1 <= k and r < len(t):
        temp += t[r]
        if r + 1 < len(t):
            temp += t[r + 1]
        r += 2
    result = max([temp, result])

    if r == l:
        r += 2
        if r - l < len(t):
            temp += t[r - 1] 
    else:
        temp -= t[l]
        if l - 1 > 0:
            temp -= t[l - 1]

print(result)
