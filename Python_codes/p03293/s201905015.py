s = input()
t = input()
for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit()
    else:
        pass
print("No")