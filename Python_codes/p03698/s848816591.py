s = input()
ls = []
ans = 1

for i in range(len(s)):
    if s[i] not in ls:
        ls.append(s[i])
    else:
        ans = 0
        break

if ans == 0:
    print("no")
else:
    print("yes")
