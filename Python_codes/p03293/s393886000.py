s = input()
t = input()
flag = False
for i in range(len(s)):
    if s == t:
        flag =True
    s = s[-1] + s[0:len(s)-1]
if flag:
    print("Yes")
else:
    print("No")
