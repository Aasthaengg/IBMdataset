s = input().replace('BC','D')
d = 0
ans = 0
for c in s[-1::-1]:
    if c == 'D':
        d += 1
    elif c == 'A':
        ans += d
    else:
        d = 0
print(ans)