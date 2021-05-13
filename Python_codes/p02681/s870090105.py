import re


s = input()
t = input()

ans = 'No'

if re.match((s + r'\w'), t):
    ans = 'Yes'

print(ans)
