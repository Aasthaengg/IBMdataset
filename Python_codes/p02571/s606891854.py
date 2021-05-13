s=str(input())
s1=str(input())
l=[]
for i in range(0,len(s)-len(s1)+1):
    e=s[i:i+len(s1)]
    f=0
    for j in range(0,len(e)):
        if(e[j]!=s1[j]):
            f=f+1
    l.append(f)
print(min(l))