n=int(input())
c1=0
c2=0
c3=0
ans=0
for i in range(n):
    s=input()
    if s[0]=="B" and s[-1]=="A":
        c1+=1
    if s[0]=="B" and s[-1]!="A":
        c2+=1
    if s[0]!="B" and s[-1]=="A":
        c3+=1
    for j in range(len(s)-1):
        if s[j]=="A"and s[j+1]=="B":
            ans+=1
if c1==0:
    ans+=min(n-1,min(c2,c3))
elif c1!=0:
    if c2+c3>0:
        ans+=c1+min(c2,c3)
    if c2+c3==0:
        ans+=c1-1
print(ans)