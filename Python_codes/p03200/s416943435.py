s = input()
black = 0
ans = 0

for i in range(len(s)):
    if s[i] == 'W':
        ans += black
    else:
        black += 1

print(ans)
