s=input()
if "".join(s[:3:])==s[0]*3 or "".join(s[1::])==s[3]*3:
    print("Yes")
else:
    print("No")