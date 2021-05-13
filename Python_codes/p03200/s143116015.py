s = list(input())

ans = 0
black = 0

for i in range(len(s)):
    if s[i] == 'W':
        ans += i - black
        black += 1

print(ans)