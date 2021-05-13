# Written by Shagoto
s = input()
i = 0
check = True
while(i < len(s)):
    if(i % 2 == 0 and s[i] == "L"):
        check = False
        break
    elif(i % 2 == 1 and s[i] == "R"):
        check = False
        break
    i += 1

if(check):
    print("Yes")
else:
    print("No")