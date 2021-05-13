s=str(input())
for i in range(len(s)):
    if s[i]=="A":
        x=i
        break
for j in range(len(s)-1,-1,-1):
    if s[j]=="Z":
        y=j
        break

print(y-x+1)