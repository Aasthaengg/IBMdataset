S=list(input())
ki=[]
gu=[]
for i in range(len(S)):
    if i%2==0:
        ki.append(S[i])
    else:
        gu.append(S[i])
if ("L" not in ki) and ("R" not in gu):
    print("Yes")
else:
    print("No")