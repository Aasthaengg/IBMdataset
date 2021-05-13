s = input()
a=len(s)
z=0
for i in  range(len(s)):
    if s[i]=="A":
        if i<a:
            a=i
    if s[i]=="Z":
        if i>z:
            z=i
print(z-a+1)