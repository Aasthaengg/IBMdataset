import itertools
S=input()
N=len(S)
flag=0
s="AKIHABARA"
s2=""
l2=[]
count=0
for i in range(9):
    l=list((itertools.combinations(s,i+1)))
    #print(l)
    for j in range(len(l)):
        s2="".join(l[j])
        l2.append(s2)
for i in range(len(l2)):
    if l2[i]==S:
        for j in range(len(l2[i])):
            if l2[i][j]=="A":
                count=count+1
        if (4-count)+len(l2[i])==9:
            flag=1
        break
if flag==1:
    print("YES")
else:
    print("NO")

