n=int(input())
s=str(input())
t=str(input())
listed=[]
cnt=0
while cnt<=n-1:
    if s[cnt]==t[cnt]:
        cnt+=1
        listed.append("T")
    elif s[cnt]==s[cnt+1] and t[cnt]==t[cnt+1]:
        cnt+=2
        listed.append("Y")

length=len(listed)
if listed[0]=="T":
    ans=3
elif listed[0]=="Y":
    ans=6
for i in range(0,length-1):
    
    if listed[i]=="Y" and listed[i+1]=="Y":
        ans=ans*3%(10**9+7)
    
    if listed[i]=="Y" and listed[i+1]=="T":
        ans=ans
        
    if listed[i]=="T" and listed[i+1]=="Y":
        ans=ans*2%(10**9+7)
        
        
    if listed[i]=="T" and listed[i+1]=="T":
        ans=ans*2%(10**9+7)
print(ans)