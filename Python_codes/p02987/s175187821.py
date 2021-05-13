s=input()
s=sorted(s)
if s[0]==s[1] and s[2]==s[3]:
    if s[0]==s[2]:
        print("No")
    else:
        print("Yes")
else:
    print("No")