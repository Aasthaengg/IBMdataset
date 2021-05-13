s=input()
b=input()
c=0
for i in range(len(s)):
    if s[i]!=b[i]:
        c=c+1
    else:
        pass
print(c)