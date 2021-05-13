s = list(input())

if len(set(s)) != 2:
    ans = 'No'
else:
    if s.count(s[0]) == 2:
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)