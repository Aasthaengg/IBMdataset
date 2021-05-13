s = input()
ans = 'None'
for i in range(26):
    c = chr(ord('a') + i)
    if c not in s:
        ans = c
        break
print(ans)
