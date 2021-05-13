s=input()
d={}
for i in range(int(len(s))):
    if s[i] not in d:
        d[s[i]]=1
    else:
        print("no")
        exit()
print("yes")