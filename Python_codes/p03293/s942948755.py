s = input()
t = input()
c = 'No'
for i in range(len(s)):
    s = s[len(s)-1] + s[:len(s)-1]
    if s == t:
        c = 'Yes'
        break

print(c)
