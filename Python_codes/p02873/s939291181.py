s=input()
cnt=0
if s[0]=="<":
    cnt=1
else:
    cnt=-1
l=[]
for i in range(len(s)-1):
    if s[i]=="<":
        if s[i+1]=="<":
            cnt+=1
        else:
            l.append(cnt)
            cnt=-1
    else:
        if s[i+1]==">":
            cnt-=1
        else:
            l.append(cnt)
            cnt=1
l.append(cnt)
ans=0
for i in range(len(l)-1):
    if l[i]>0 and l[i+1]<0:
        a=abs(l[i])
        b=abs(l[i+1])
        ans+=max(a,b)
        ans+=(a-1)*a//2+(b-1)*b//2

if l[0]<0:
    ans+=(abs(l[0])+1)*abs(l[0])//2

if l[-1]>0:
    ans+=(l[-1]+1)*l[-1]//2
print(ans)