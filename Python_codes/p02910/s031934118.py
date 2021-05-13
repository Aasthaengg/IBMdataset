s=input()
o="RUD"
e="LUD"
for i in range(0,len(s),2):
    if s[i] not in o:
        print("No")
        exit()
for i in range(1,len(s),2):
    if s[i] not in e:
        print("No")
        exit()
print("Yes")