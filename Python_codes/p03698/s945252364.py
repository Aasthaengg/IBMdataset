s = input()

cha = []

for i in range(len(s)):
    if s[i] in cha:
        print("no")
        exit()
    else:
        cha.append(s[i])

print("yes")
