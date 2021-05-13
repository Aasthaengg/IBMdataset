n=int(input())
s=[ str(input()) for _ in range(n)]
ans=0
a=0
b=0
ab=0
for i in range(n):
    for j in range(len(s[i])-1):
        if s[i][j:j+2]=="AB":
            ans+=1
#print(ans)
for i in range(n):
    if s[i][0]=="B" and s[i][-1]=="A":
        ab+=1
    elif s[i][0]=="B":
        b+=1
    elif s[i][-1]=="A":
        a+=1

ma=max(a,b)
mi=min(a,b)
if 1<=a :
    ans+=ab
else:
    if 1<=ab:
        a+=1
        ab-=1
        ans+=ab

ans+=min(a,b)

#print(a,b,ab)
print(ans)