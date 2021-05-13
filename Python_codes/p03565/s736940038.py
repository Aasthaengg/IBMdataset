s=input()
t=input()
l=[]
check=0
for i in range(len(s)-len(t)+1):
    c=0
    for j in range(len(t)):
        if s[i+j]!=t[j] and s[i+j]!="?":
            break
        else:
            c+=1
    if c==len(t):
        check+=1
        l.append(s[:i]+t+s[i+j+1:])
    #print(c)
#print(l)
if check==0:
    print("UNRESTORABLE")
else:
    L=[]
    for i in range(len(l)):
        x=""
        for j in range(len(s)):
            if l[i][j]=="?":
                x+="a"
            else:
                x+=l[i][j]
        L.append(x)
    L.sort()
    print(L[0])