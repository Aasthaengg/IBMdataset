s=list(input())
n=len(s)
ind=[]
count=[]
temp=0
for i in range(n-1):
    temp+=1
    if s[i]!=s[i+1] and s[i]=="R":
        count.append(temp)
        ind.append(i)
        temp=0
    if s[i]!=s[i+1] and s[i]=="L":
        count.append(temp)
        temp=0
    if i==n-2:
      count.append(temp+1)

ans=[0]*n
for j in range(len(ind)):
    if (count[2*j]+count[2*j+1])%2==1:
        if count[2*j]%2==0:
            ans[ind[j]]+=(count[2*j]+count[2*j+1])//2
            ans[ind[j]+1]+=((count[2*j]+count[2*j+1])//2+1)
        else:
            ans[ind[j]]+=((count[2*j]+count[2*j+1])//2+1)
            ans[ind[j]+1]+=(count[2*j]+count[2*j+1])//2
    else:
        ans[ind[j]]+=(count[2*j]+count[2*j+1])//2
        ans[ind[j]+1]+=(count[2*j]+count[2*j+1])//2
ans2=[]
for k in range(n):
    ans2.append(str(ans[k]))
print(" ".join(ans2))