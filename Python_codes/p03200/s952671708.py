s = input()
ans = 0
tmp = 0
for c in s:
    if c == 'B':
        tmp += 1
    else:
        ans += tmp
print(ans)