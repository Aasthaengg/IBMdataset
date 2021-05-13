s = input()
count = 0
if len(set(s)) == 1:
    print(0)
    exit()
left = 0
right = len(s) - 1

ans = 0
while True:
    if (s[left] == 'x' and s[right] == 'x') or s[left] == s[right]:
        left += 1
        right -= 1
    elif s[left] == 'x' and s[right] != 'x':
        ans += 1
        left += 1
    elif s[left] != 'x' and s[right] == 'x':
        ans += 1
        right -= 1
    elif s[left] != 'x' and s[right] != 'x' and s[left] != s[right]:
        print(-1)
        exit()
    if right <= left:
        break
print(ans)
