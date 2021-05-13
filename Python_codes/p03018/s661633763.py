s=list(input())
l=[]
f=0
for i in range(len(s)-1):
    if s[i]=="A":
        l.append("A")
        f=0
    elif s[i]=="B":
        if s[i+1]=="C":
            l.append("D")
            f=1
        else:
            l.append("B")
            f=0
    else:
        if f:
            f=0
            continue
        else:
            l.append("C")
ac=0
ans=0
for i in range(len(l)):
    if l[i]=="A":
        ac+=1
    elif l[i]=="D":
        ans+=ac
    else:
        ac=0
print(ans)
