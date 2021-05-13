s = input()
ans = 'Yes'
for i in range(len(s)):
    if i%2 and not(s[i] in 'LUD'):
        ans = 'No'
        break
    if not(i%2) and not(s[i] in 'RUD'):
        ans = 'No'
        break
print(ans)
