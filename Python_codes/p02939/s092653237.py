s = input()
l = [s[0]]
x = ""
for i in range(1,len(s)):
    if x == "": x = s[i]
    else: x += s[i]
    if l[-1] != x:
        l.append(x)
        x = ""
print(len(l))