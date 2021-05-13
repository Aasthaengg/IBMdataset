# Written by Shagoto

s = input()
s = s.replace(s[0], "")

if(len(s) == 2):
    s = s.replace(s[0], "")
    if(len(s) == 0):
        print("Yes")
    else:
        print("No")
else:
    print("No")