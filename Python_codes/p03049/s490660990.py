n=int(input())
a=0
b=0
ab=0
ans=0
for i in range(n):
    s=input()
    m=len(s)
    m-=len(s.replace("AB",""))
    m//=2
    ans+=m
    if s[0]=="B" and s[-1]=="A":
        ab+=1
    elif s[0]=="B":
        b+=1
    elif s[-1]=="A":
        a+=1

if a+b>0:
    print(ans+min(a,b)+ab)
else:
    print(ans+max(0,ab-1))