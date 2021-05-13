n,k=map(int,input().split())
s=input()
ban=[]
if s[0]=="0": ban.append(0)
cnt=1
for i,val in enumerate(s[:-1]):
    if val!=s[i+1]:
        ban.append(cnt)
        cnt=0
    cnt+=1
if cnt>0: ban.append(cnt)
if s[n-1]=="0": ban.append(0)
ans=sum(ban[0:2*k+1])
su=ans
now=0
while now+2*k+2<=len(ban):
    su-=ban[now]+ban[now+1]
    su+=ban[now+2*k+1]+ban[now+2*k+2]
    if su>ans: ans=su
    now+=2
print(ans)