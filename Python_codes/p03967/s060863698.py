s = input()

ans = 0
for index in range(len(s)):
    if s[index] == 'g':
        ans += 1
    else:
        ans -= 1


print(ans // 2)