s = input()
ans = 0
b = 0
for c in s:
    if c == 'W':
        ans += b
    elif c == 'B':
        b += 1
print(ans)