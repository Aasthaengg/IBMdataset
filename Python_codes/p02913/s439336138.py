n=int(input())
s=input()

suc=[0]*(n-1)
ans=0
for i,c in enumerate(s):
    for j in range(n-1):
        idx=(i+1+j)%n
        if idx==0:
            suc[j]=0#またぐのは禁止
        if c==s[idx]:
            suc[j]+=1
            suc[j]=min(suc[j],j+1,n-1-j)#最大j+1を超えると重なるため
            ans=max(ans,suc[j])
        else:
            suc[j]=0
print(ans)