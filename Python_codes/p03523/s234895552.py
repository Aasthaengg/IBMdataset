s=list(input())
k=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        print("NO")
        exit()
    if s[i]=="K" and s[i+1]!="I":
        print("NO")
        exit()
    if s[i]=="I" and s[i+1]!="H":
        print("NO")
        exit()

for i in range(len(s)):
    if s[i]!="A":
        k.append(s[i])
if k==["K","I","H","B","R"]:
    print("YES")
else:
    print("NO")

