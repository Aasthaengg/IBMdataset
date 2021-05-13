# 3:06
s = input()
out = True
for c in s[1:]:
    if c != '9':
        out = False
        break

if out:
    print(int(s[0]) + (len(s) - 1) * 9)
else:
    print(int(s[0]) - 1 + (len(s) - 1) * 9)
