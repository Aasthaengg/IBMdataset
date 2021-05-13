n,k=map(int,input().split())
s=input()
A=[]
now=1
cnt=0
for i in range(n):
    if int(s[i])==now:
        cnt+=1
    else:
        now^=1
        A.append(cnt)
        cnt=1
A.append(cnt)
if len(A)%2==0:
    A.append(0)



bk=2*k+1
ans=sum(A[0:bk])
res=ans
left=0
right=bk
while right+2<=len(A):
    res-=A[left]
    res-=A[left+1]
    left+=2    
    res+=A[right]
    res+=A[right+1]
    right+=2
    ans=max(res,ans)
print(ans)
    

