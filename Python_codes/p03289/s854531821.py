import string

s = list(input())
flag = True
if s[0] != "A":
    flag = False
count = 0
for i in range(1, len(s)):
    if s[i] in string.ascii_uppercase:
        if i == 1 or i == len(s) - 1 or s[i] != "C":
            flag = False
        count += 1

if flag and count == 1:
    print("AC")
else:
    print("WA")
