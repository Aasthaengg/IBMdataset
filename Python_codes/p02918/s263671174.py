n,k=map(int,input().split())
s=input()
ans=0
bef=s[0]
cnt=0
s2_l=[s[0]]
for i in range(n):
    if bef==s[i]:
        cnt+=1
    else:
        ans+=(cnt-1)
        cnt=1
        bef=s[i]
        s2_l.append(bef)
    if i==n-1:
        ans+=(cnt-1)
s2="".join(s2_l)
n2=len(s2)
if n2==1:
    print(ans)
    exit()
if s2[0]==s2[n2-1]:
    print(ans+min(k,s2.count(s2[1]))*2)
else:
    if k>=n2//2:
        print(ans+n2-1)
    else:
        print(ans+k*2)
    
