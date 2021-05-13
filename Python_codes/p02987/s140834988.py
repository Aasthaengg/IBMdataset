s = input()
sd = s[::-1]
ans = 'No'
if len(set(s)) == 2:
    c = 0
    for i in range(4):
        if s[i] == sd[i]:
            c += 1
    if c%2 == 0:
        ans = 'Yes'
print(ans)
