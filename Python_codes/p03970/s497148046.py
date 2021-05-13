s=list(input())
t=list("CODEFESTIVAL2016")
c=0
for x in range(16):
    if t[x]!=s[x]:c+=1
print(c)