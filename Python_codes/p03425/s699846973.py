n = int(input())

l = [0] * 5
for i in range(n):
    s = list(input())
    if s[0] == 'M':
        l[0] += 1
    elif s[0] == 'A':
        l[1] += 1
    elif s[0] == 'R':
        l[2] += 1
    elif s[0] == 'C':
        l[3] += 1
    elif s[0] == 'H':
        l[4] += 1

ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += (l[i] * l[j] * l[k])

print(ans)