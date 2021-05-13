n=int(input())
#s=[]
l=[0]*5
#print(l)
for _ in range(n):
    s=input()
    if s[0]=="M": l[0]+=1
    if s[0]=="A": l[1]+=1
    if s[0]=="R": l[2]+=1
    if s[0]=="C": l[3]+=1
    if s[0]=="H": l[4]+=1
#print(l)
ans=0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i!=j and j!=k and k!=i:
                ans+=l[i]*l[j]*l[k]
ans//=6
print(ans)
