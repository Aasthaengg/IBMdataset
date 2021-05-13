s = input()
ans = 0
left = 0
right = len(s) - 1
while left <= right:
    if s[left] != s[right]:
        if s[left] == "x":
            right += 1
        elif s[right] == "x":
            left -= 1
        else:
            ans = -1
            break
        ans += 1
    left += 1
    right -= 1

print(ans)