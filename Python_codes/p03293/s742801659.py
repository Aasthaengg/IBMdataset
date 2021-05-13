s = str(input())
t = str(input())
z = 'No'
for i in range(len(s)):
    w = s[i:] + s[:i]
    if w == t:
        z = 'Yes'
        break
print(z)