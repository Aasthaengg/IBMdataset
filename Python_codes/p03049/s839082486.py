N=int(input())

ba=0
_a=0
b_=0

ans=0
for i in range(N):
    s=input()
    ans+=s.count("AB")
    if s[0]=="B" and s[-1]=="A":
        ba+=1
    elif s[-1]=="A":
        _a+=1
    elif s[0]=="B":
        b_+=1

#print(ans)

if ba>0:
    ans+=(ba-1)
    if _a>0:
        _a-=1
        ans+=1
    if b_>0:
        b_-=1
        ans+=1

ans+=min(_a,b_)

print(ans)