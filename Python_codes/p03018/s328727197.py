s = input()
d = []
i = 0
while i < len(s)-1:
    if s[i] == 'B' and s[i+1] == 'C':
        d.append('D')
        i += 2
    else:
        d.append(s[i])
        i += 1
ans = 0
x = 0
for i in range(len(d)):
    if d[i] == 'A':
        x += 1
    elif d[i] == 'D':
        ans += x
    else:
        x = 0
print(ans)