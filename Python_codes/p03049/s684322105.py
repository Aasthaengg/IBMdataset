N=int(input())

ab=0
a=0
b=0
boa=0

for _ in range(N):
    s=input()
    ab+=s.count("AB")
    if s[0]=="B" and s[-1]=="A":
        boa+=1
    elif s[0]=="B":
        b+=1
    elif s[-1]=="A":
        a+=1
ans=ab

if boa>0:
    ans+=boa-1
    if b>0:
        ans+=1
        b-=1
    if a>0:
        ans+=1
        a-=1
ans+=min(a,b)
print(ans)