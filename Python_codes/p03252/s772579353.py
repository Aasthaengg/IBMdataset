from collections import defaultdict

s=input()
t=input()
lis=defaultdict(lambda:"A")
lis2=defaultdict(lambda:"A")
for i,val in enumerate(s):
    if lis[val]=="A":
        lis[val]=t[i]
    else:
        if lis[val]!=t[i]:
            print("No")
            exit()
for i,val in enumerate(t):
    if lis2[val]=="A":
        lis2[val]=s[i]
    else:
        if lis2[val]!=s[i]:
            print("No")
            exit()
print("Yes")