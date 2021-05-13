N=int(input())
s=[]
for i in range(N):
    S=input()
    s.append(S)

sm=0

for i in range(N):
    count=0
    tmp=-1
    for j in range(len(s[i])):
        if s[i][j]=="A":
            tmp=1
        elif s[i][j]=="B":
            if tmp==1:
                count+=1
            tmp=-1
        else:
            tmp=-1
    sm+=count
chk=[0 for _ in range(N)]
for i in range(N):
    if s[i][0]=="B" and s[i][-1]=="A":
        chk[i]=3
    elif s[i][-1]=="A":
        chk[i]=2
    elif s[i][0]=="B":
        chk[i]=1
x=0
y=0
z=0
#print(sm)
ans=sm
for i in range(N):
    if chk[i]==3:
        z+=1
    if chk[i]==2:
        x+=1
    if chk[i]==1:
        y+=1
if z>0:
    a=z-1
    ans+=a
    if x>0:
        ans+=1
        x-=1
    if y>0:
        ans+=1
        y-=1
ans+=min(x,y)
print(ans)