s=input()
first=-1
last=0
for i in range(len(s)):
    if s[i]=="A":
        first=i
        break
for j in range(len(s)-1,-1,-1):
    if s[j]=="Z":
        last=j
        break

print(j-i+1)
