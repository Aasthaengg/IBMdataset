s = input()
y = input()

s_s = sorted(s)
y_s = sorted(y,reverse=True)
if("".join(s_s)<"".join(y_s)):
    print("Yes")
else:
    print("No")