s=input()
t=input()
for i in range(len(s)):
    s=s[1:len(s)]+s[0]
    if t==s:
        print("Yes")
        break
else:
    print("No")