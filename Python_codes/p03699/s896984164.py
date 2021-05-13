n=int(input())
s=[]
ans=-1
for i in range(n):
    s.append(int(input()))
sums=sum(s)
if sums%10!=0:
    print(sums)
    exit()
for i in range(n):
    tmp=0 if (sums-s[i])%10==0 else sums-s[i]
    ans=max(ans,tmp)
print(ans)