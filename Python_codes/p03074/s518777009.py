n,k=map(int,input().split())
s=input()

flag=1
i=0
ans=[0]*(n+1)
for ss in s:
    if int(ss)==flag:
        ans[i]+=1
    else:
        i+=1
        ans[i]+=1
        flag=(flag+1)%2

result=(sum(ans[:min(2*k+1,n)]))

tmp=result

l=0
r=2*k
#print(ans)
while 1:
    if r+2<(n+1):
        tmp=tmp-ans[l]-ans[l+1]+ans[r+1]+ans[r+2]
        l+=2
        r+=2
        result=max(result,tmp)
        #print(ans[l:r])
    else:
        break

    #print(tmp)
print(result)