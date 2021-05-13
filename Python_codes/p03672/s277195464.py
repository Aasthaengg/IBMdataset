s = input()
s = s[:- 2]
t = len(s) // 2
for i in range(t):
    if s[0:len(s) // 2] == s[len(s) // 2:]:
        print(len(s))
        break
    else:
        s = s[:- 2]