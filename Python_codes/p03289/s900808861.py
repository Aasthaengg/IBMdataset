s = input()
ans = "AC"
c = 0
for i in range(len(s)):
    if i==0 and s[i]!="A":
        ans = "WA"
    if i>=2 and i<len(s)-1:
        if s[i]=="C":
            c += 1
        elif ord(s[i])>=65 and ord(s[i])<=90:
            ans = "WA"
    if i==1 or i==len(s)-1:
        if ord(s[i])>=65 and ord(s[i])<=90:
            ans = "WA"
if c!=1:
    ans = "WA"
print(ans)