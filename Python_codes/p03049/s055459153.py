

N=int(input())
L=[] #(lastA, firstB, have AB)
ans=0
lastA=0
firB=0
AB=0
for i in range(N):
    s=input()
    c=s.count("AB")
    #print(c)
    a=s[-1]=="A"
    b=s[0]=="B"
    d=(a==b==1)
    if d:
        a=0
        b=0
    ans+=c
    lastA+=a
    firB+=b
    AB+=d

if lastA and firB:
    ans+=2+AB-1
    lastA-=1
    firB-=1
    ans+=min(lastA, firB)
elif lastA or firB:
    ans+=AB
else:
    ans+=max(AB-1,0)
print(ans)