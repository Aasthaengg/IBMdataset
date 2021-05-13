n=int(input())
s=[]
ans=0
for i in range(n):
    x=int(input())
    ans+=x
    if x%10!=0:s.append(x)
s=sorted(s)
if ans%10==0:
    if len(s)>=1:
        print(ans-s[0])
    else:
        print(0)
else:
    print(ans)

