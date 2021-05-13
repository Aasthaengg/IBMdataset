s = input()
sr = s[-1::-1]
left = 0
right = 0
ans = 0
while (1):
    if left + right >= len(s) - 1:
        break
    if s[left] != sr[right]:
        if s[left] == 'x':
            left += 1
        elif sr[right] == 'x':
            right += 1
        else:
            print(-1)
            exit()
        ans += 1
    elif s[left] == sr[right]:
        left += 1
        right += 1

print(ans)
