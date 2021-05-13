s = input()
t = input()

for _ in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        ans = 'Yes'
        break
else:
    ans = 'No'

print(ans)
