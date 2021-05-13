s = list(input())
ans = 'Yes'
for i in range(len(s)):
    if i%2 == 1:
        if s[i] == 'R':
            ans = 'No'
            break
    else:
        if s[i] == 'L':
            ans = 'No'
            break
print(ans)