s = input()
ans = 0
w = 0
for i in range(len(s)):
    if (s[i] == 'W'):
        ans += i - w
        w += 1
print(ans)