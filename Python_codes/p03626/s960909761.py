n=int(input())
s=input()
s="?"+input()
mod=10**9+7

col=[]
for i in range(n):
    if s[i+1]!=s[i]:
        col.append(1)
    else:
        col[-1]+=1
    
for i in range(len(col)):
    now=col[i]
    if i==0:
        ans=3 if now==1 else 6
        continue
    bef=col[i-1]
    if bef==1:
        ans*=2
        ans%=mod
    elif bef==2 and now==2:
        ans*=3
        ans%=mod

print(ans)
        
