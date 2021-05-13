s=input()
t=s[::-1]
for i in range(len(s)):
    if s[i]=="A":
        break
for j in range(len(t)):
    if t[j]=="Z":
        break
print(len(s)-j-i)