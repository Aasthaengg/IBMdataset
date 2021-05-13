s = input()
ans = 0
for t, u in zip(s[::2], s[1::2]):
    if t == 'p':
        ans -= 1
    if u == 'g':
        ans += 1
print(ans)
